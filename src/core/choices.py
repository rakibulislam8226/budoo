from django.db import models


class UserStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PRESENT = "PRESENT", "Present"
    ABSENT = "ABSENT", "Absent"
    REMOVED = "REMOVED", "Removed"


class UserGender(models.TextChoices):
    FEMALE = "FEMALE", "Female"
    MALE = "MALE", "Male"
    UNKNOWN = "UNKNOWN", "Unknown"
    OTHER = "OTHER", "Other"
