from rest_framework import status

from common.base_test import BaseAPITestCase

from ..models import User, UserStatus
from . import payloads
from . import urlhelpers


class UserDetailViewTests(BaseAPITestCase):
    def setUp(self):
        super(BaseAPITestCase, self).setUp()
        # Create a superuser
        self.superuser = User.objects.create_superuser(**payloads.super_user_payload())
        # Log in as the superuser
        self.client.login(**payloads.superuser_login_payload())

    @classmethod
    def setUpTestData(cls):
        cls.absent_user = User.objects.create(**payloads.absent_user_payload())

    def test_user_detail_get_api(self):
        """Test retrieving user detail"""
        response = self.client.get(f"/users/{self.absent_user.email}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["phone"], "+8801111111112")
        self.assertEqual(data["status"], UserStatus.ABSENT)
        self.assertEqual(data["email"], "testabsent@mail.com")

    def test_user_detail_patch_api(self):
        """Test updating user detail"""

        response = self.client.patch(
            urlhelpers.user_detail_url(self.absent_user.email),
            payloads.update_user_payload(),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["status"], UserStatus.ABSENT)
