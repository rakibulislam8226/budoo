from rest_framework import status

from common.base_test import BaseAPITestCase

from . import payloads
from . import urlhelpers
from ..models import User, UserStatus


class UserListViewTests(BaseAPITestCase):
    def setUp(self):
        super(BaseAPITestCase, self).setUp()

    def test_user_api(self):
        """Test retrieving users without any status filter"""
        response = self.client.get("/users")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        phone = [user["phone"] for user in data["results"]]
        self.assertIn("+8801111111112", phone)
        self.assertIn("+8801111111113", phone)
        self.assertEqual(len(data["results"]), 2)

    def test_user_present_tab_api(self):
        """Test retrieving users with present status"""
        response = self.client.get("/users?status=present")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn(data["results"][0]["status"], UserStatus.PRESENT)

    def test_user_absent_tab_api(self):
        """Test retrieving users with absent status"""
        response = self.client.get("/users?status=absent")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn(data["results"][0]["status"], UserStatus.ABSENT)
