import logging

from rest_framework.test import APIClient, APITestCase

from core.models import User
from django.contrib.auth import get_user_model

from core.test import payloads

logger = logging.getLogger(__name__)


class BaseOrmCallApi(APITestCase):
    def get_user(self) -> User:
        logger.warning("Created super USER with ORM calls")

        return get_user_model().objects.create_superuser(
            **payloads.super_user_payload()
        )
