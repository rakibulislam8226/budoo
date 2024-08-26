import logging
import os

from django.db import transaction

from celery import shared_task

from contentio.choices import LogTypeChoices, LogStatusChoices
from contentio.models import LogsTracking

from .choices import UserStatus
from .models import User

logging.basicConfig(level=logging.INFO)


@shared_task(bind=True, max_retries=3)
def update_active_user_status_to_present(self):
    """
    Updates the status of active users to present in batches and logs the outcome.
    """
    try:
        total_active_users = User.objects.filter(is_active=True).count()

        if total_active_users == 0:
            return

        batch_size = int(os.getenv("BATCH_SIZE", 1000))
        status = LogStatusChoices.SUCCESS
        error_details = None

        for offset in range(0, total_active_users, batch_size):
            update_batch_wise_status_to_present.delay(offset, batch_size)

    except Exception as e:
        status = LogStatusChoices.FAILED
        error_details = str(e)
        store_final_log.delay(status=status, error_details=error_details)
        return

    store_final_log.delay(status=status, error_details=error_details)


@shared_task(bind=True, max_retries=3)
def update_batch_wise_status_to_present(self, offset, limit):
    """
    Update the status of active users based on the offset and limit. Limit means batch size here.
    """
    try:
        with transaction.atomic():
            if user_ids := User.objects.filter(is_active=True).values_list(
                "id", flat=True
            )[offset : offset + limit]:
                User.objects.filter(id__in=user_ids).update(status=UserStatus.PRESENT)

            else:
                return

    except Exception as e:
        logging.error(
            f"Failed to update users at offset {offset} with limit {limit}: {str(e)}"
        )
        store_final_log.delay(
            status=LogStatusChoices.FAILED,
            error_details=f"Failed to update users at offset: {offset} with limit: {limit}. - {str(e)}",
        )
        self.retry(exc=e, countdown=60)


@shared_task
def store_final_log(status, error_details=None):
    """
    Store the final log after the operation is complete.
    """
    log_data = {
        "task": "update_active_user_status_to_present",
        "error_details": error_details or "",
    }
    LogsTracking.objects.create(
        log_data=log_data,
        status=status,
        log_type=LogTypeChoices.ATTENDANCE,
    )
