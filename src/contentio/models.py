from django.db import models
from django.conf import settings

from common.models import BaseModelWithUID

from .choices import LogTypeChoices, LogStatusChoices


# Create your models here.
class LogsTracking(BaseModelWithUID):
    """
    Logs tracking model to store the logs of the system
    """

    log_type = models.CharField(
        max_length=255,
        choices=LogTypeChoices.choices,
        default=LogTypeChoices.OTHER,
    )
    status = models.CharField(
        max_length=255,
        choices=LogStatusChoices,
        default=LogStatusChoices.PENDING,
    )
    log_data = models.JSONField()

    class Meta:
        verbose_name = "Logs Tracking"
        verbose_name_plural = "Logs Tracking"

    def __str__(self):
        return f"{self.log_type} - {self.created_at}"
