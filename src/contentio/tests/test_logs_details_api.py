from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from core.models import User
from core.test import payloads as core_payloads
from . import payloads
from . import urlhelpers
from ..choices import LogStatusChoices, LogTypeChoices
from ..models import LogsTracking


class LogTrackingDetailsViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a superuser
        self.superuser = User.objects.create_superuser(
            **core_payloads.super_user_payload()
        )
        # Log in as the superuser
        self.client.login(**core_payloads.superuser_login_payload())

    @classmethod
    def setUpTestData(cls):
        cls.success_logs = LogsTracking.objects.create(
            **payloads.success_logs_payload()
        )
        cls.failed_logs = LogsTracking.objects.create(**payloads.failed_logs_payload())

    def test_logs_detail_get_api(self):
        """Test retrieving logs detail"""
        response = self.client.get(urlhelpers.logs_detail_url(self.success_logs.uid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["log_type"], LogTypeChoices.ATTENDANCE)
        self.assertEqual(data["status"], LogStatusChoices.SUCCESS)
