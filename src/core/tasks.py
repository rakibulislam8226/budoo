import os, logging

from celery import shared_task
from .models import User
from .choices import UserStatus

logging.basicConfig(level=logging.INFO)


@shared_task
def update_active_user_status_to_present():
    """
    This task updates the status of active users to present with batche wise.
    """
    batch_size = int(os.getenv("BATCH_SIZE", 1000))
    active_users = User.objects.filter(is_active=True).values_list("id", flat=True)
    total_users = len(active_users)

    for i in range(0, total_users, batch_size):
        batch_ids = active_users[i : i + batch_size]
        User.objects.filter(id__in=batch_ids).update(status=UserStatus.PRESENT)
        logging.info(f"Updated status of users from {i} to {i + batch_size} to present")

    return f"Batch update for {total_users} active users completed"
