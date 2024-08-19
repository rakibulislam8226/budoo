from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from core.models import User
from core.test import payloads as core_payloads
from . import payloads
from . import urlhelpers
from ..choices import LogStatusChoices
from ..models import LogsTracking


class LogTrackingListViewTests(APITestCase):
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

    def test_log_tracking_list_api(self):
        """Test retrieving logs without any status filter"""
        response = self.client.get(urlhelpers.logs_list_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        result = [
            logs["status"] for logs in data["results"]
        ]  # Get the status of each log
        self.assertIn("success", result)
        self.assertIn("failed", result)
        self.assertEqual(len(data["results"]), 2)

    def test_logs_success_tab_api(self):
        """Test retrieving logs with success status"""
        response = self.client.get(f"{urlhelpers.logs_list_url()}?status=success")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn(data["results"][0]["status"], LogStatusChoices.SUCCESS)

    def test_logs_failed_tab_api(self):
        """Test retrieving logs with failed status"""
        response = self.client.get(f"{urlhelpers.logs_list_url()}?status=failed")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn(data["results"][0]["status"], LogStatusChoices.FAILED)
