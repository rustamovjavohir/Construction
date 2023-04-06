from django.test import TestCase
from apps.auth_user.models import CustomUser
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="test",
            email="test@gmail.com",
            telegram_id=123456789,
            photo="user_photo/1.jpg",
        )

    def test_user(self):
        self.assertEqual(self.user.username, "test")
        self.assertEqual(self.user.email, "test@gmail.com")
        self.assertEqual(self.user.telegram_id, 123456789)
        self.assertEqual(self.user.photo, "user_photo/1.jpg")


class SimpleJWTTest(APITestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)

    def test_token_obtain(self):
        url = reverse('login')
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('success' in response.data)
        self.assertTrue('refresh' in response.data.get('result'))
        self.assertTrue('access' in response.data.get('result'))

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        url = reverse('refresh_token')
        data = {'refresh': str(refresh)}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data.get('result'))
