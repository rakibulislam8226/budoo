from django.db import models
from common.models import BaseModelWithUID

from core.choices import UserStatus


# Create your models here.
class Attendence(BaseModelWithUID):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.ABSENT,
    )

    def __str__(self):
        return f"{self.user} - {self.status}"
