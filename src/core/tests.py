from rest_framework import status
from rest_framework.test import APITestCase

from .models import User, UserStatus


class UserListViewTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.absent_user = User.objects.create(
            username="+8801911111111",
            phone="+8801911111111",
            email="testabsent@mail.com",
            password="rakib123",
            status=UserStatus.ABSENT,
        )
        cls.present_user = User.objects.create(
            username="+8801911111112",
            phone="+8801911111112",
            email="testpresent@mail.com",
            password="rakib123",
            status=UserStatus.PRESENT,
        )

    def test_user_api(self):
        """Test retrieving users without any status filter"""
        response = self.client.get("/users")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        phone = [user["phone"] for user in data["results"]]
        self.assertIn("+8801911111111", phone)
        self.assertIn("+8801911111112", phone)
        self.assertEqual(len(data["results"]), 2)
        self.assertIn(data["results"][0]["status"], UserStatus.PRESENT)

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
