from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


# class ListApartmentTest(APITestCase):
#     def setUp(self):
#         self.url = reverse('apartment-list')
#
#     def test_list(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
