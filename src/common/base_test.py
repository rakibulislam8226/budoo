from rest_framework.test import APIClient, APITestCase

from core.models import User
from core.test import payloads

from .base_orm import BaseOrmCallApi


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_orm = BaseOrmCallApi()
        self.user = self.base_orm.get_user()

    @classmethod
    def setUpTestData(cls):
        cls.absent_user = User.objects.create(**payloads.absent_user_payload())
        cls.present_user = User.objects.create(**payloads.present_user_payload())
