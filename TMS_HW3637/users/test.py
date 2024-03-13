import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf.settings")
django.setup()

from requests.auth import HTTPBasicAuth
from django.test import TestCase

from django.utils.dateparse import parse_datetime
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.hashers import make_password

from django.utils import timezone
import json
from events.models import Event
from users.models import User




class UsersTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser('admin1', 'admin1@example.com', 'admin')
        self.normal_user = User.objects.create_user('test321', 'test321@example.com', 'user123')

    def test_register_user(self):
        data = {"username": "oleg", "email": "oleg@mail.com", "password": "oleg123"}
        response = self.client.post('/api/users/users/', data, format='json')
        self.assertEqual(response.status_code, 201)


    def test_superuser_can_view_list_users(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/api/users/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_view_list_users(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get('/api/users/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_incorrect_register_user(self):
        data = {"username": 'A', 'email': 'anton.mail', 'password': 'hi'}
        response = self.client.post('/api/users/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_register_user(self):
        data = {"username": '', 'email': '', 'password': ''}
        response = self.client.post('/api/users/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)