from django.db import models


class LogTypeChoices(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ATTENDANCE = "ATTENDANCE", "Attendance"
    OTHER = "OTHER", "Other"

class LogStatusChoices(models.TextChoices):
    SUCCESS = "success", "Success"
    FAILED = "failed", "Failed"
    PENDING = "PENDING", "Pending"