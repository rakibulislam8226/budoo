from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModelWithUID

from .choices import UserGender, UserStatus
from .managers import CustomUserManager
from .utils import get_user_slug


# Create your models here.
class User(BaseModelWithUID, AbstractUser):
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(unique=True, db_index=True, verbose_name="Phone Number")
    slug = AutoSlugField(populate_from=get_user_slug, unique=True)
    nid = models.CharField(max_length=20, blank=True)
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.ABSENT,
    )
    gender = models.CharField(
        max_length=20,
        blank=True,
        choices=UserGender.choices,
        default=UserGender.UNKNOWN,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"Phone: {self.phone} - Status: {self.status}"
