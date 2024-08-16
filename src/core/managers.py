import logging

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

logger = logging.getLogger(__name__)


class CustomUserManager(BaseUserManager):
    def _create_user(
        self, phone, password, is_staff, is_superuser, is_active=True, **kwargs
    ):
        """
        Creates and saves a User with the given phone and password.
        """
        now = timezone.now()
        if not phone:
            raise ValueError("phone must be set!")
        user = self.model(
            username=phone,
            phone=phone,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **kwargs):
        return self._create_user(phone, password, False, False, **kwargs)

    def create_superuser(self, phone, password, **kwargs):
        return self._create_user(phone, password, True, True, **kwargs)

