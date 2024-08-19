import logging
import os

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
    batch_size = int(os.getenv("BATCH_SIZE", 1000))
    active_users = User.objects.filter(is_active=True).values_list("id", flat=True)
    status = LogStatusChoices.SUCCESS
    error_details = None

    try:
        for i in range(0, len(active_users), batch_size):
            batch_ids = list(active_users[i : i + batch_size])
            update_batch_wise_status_to_present.delay(batch_ids)
    except Exception as e:
        status = LogStatusChoices.FAILED
        error_details = str(e)
        store_final_log.delay(status=status, error_details=error_details)
        return

    store_final_log.delay(status=status, error_details=error_details)


@shared_task(bind=True, max_retries=3)
def update_batch_wise_status_to_present(self, batch_ids):
    """
    Update the status of users to present in batches.
    """
    try:
        User.objects.filter(id__in=batch_ids).update(status=UserStatus.PRESENT)
    except Exception as e:
        logging.error(f"Failed to update batch {batch_ids}: {str(e)}")
        store_final_log.delay(status=LogStatusChoices.FAILED, error_details=str(e))
        self.retry(exc=e, countdown=60)


@shared_task
def store_final_log(status, error_details=None):
    """
    Store the final log after the operation is complete.
    """
    log_data = {
        "task": "update_active_user_status_to_present",
        "error_details": error_details if error_details else "",
    }
    LogsTracking.objects.create(
        log_data=log_data,
        status=status,
        log_type=LogTypeChoices.ATTENDANCE,
    )
