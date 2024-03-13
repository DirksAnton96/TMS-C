# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf.settings")
# django.setup()

# from requests.auth import HTTPBasicAuth
# from django.test import TestCase

# from django.utils.dateparse import parse_datetime
# from rest_framework import status
# from rest_framework.test import APIClient, APITestCase
# from django.contrib.auth.hashers import make_password

# from django.utils import timezone
# import json
# from events.models import Event
# from users.models import User




# class EventTest(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()

#     def setUp(self):
#         self.client = APIClient()
#         self.admin_user = User.objects.create_superuser('admin1', 'admin1@example.com', 'admin')
#         self.normal_user = User.objects.create_user('test321', 'test321@example.com', 'user123')
#         self.past_event = Event.objects.create(name='Past Event',
#                                                meeting_time=timezone.now() - timezone.timedelta(days=1))
#         self.future_event = Event.objects.create(name='Future Event',
#                                                  meeting_time=timezone.now() + timezone.timedelta(days=1))


#     # def test_register_user(self):
#     #     data = {"username": "oleg", "email": "oleg@mail.com", "password": "oleg123"}
#     #     response = self.client.post('/api/users/users/', data, format='json')
#     #     self.assertEqual(response.status_code, 201)


#     # def test_superuser_can_view_list_users(self):
#     #     self.client.force_authenticate(user=self.admin_user)
#     #     response = self.client.get('/api/users/users/')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # def test_user_cannot_view_list_users(self):
#     #     self.client.force_authenticate(user=self.normal_user)
#     #     response = self.client.get('/api/users/users/')
#     #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_events_list(self):
#         response = self.client.get('/api/events/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         events = json.loads(response.content.decode('utf-8'))

#         for event in events:
#             event_time = parse_datetime(event['meeting_time'])
#             self.assertGreater(event_time, timezone.now())

#     def test_event_signup(self):
#         url = f'/api/events/{self.future_event.id}'
#         self.client.force_authenticate(user=self.admin_user)

#         response = self.client.post(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn(self.admin_user, self.future_event.users.all())

#     def test_past_event_signup_forbidden(self):
#         url = f'/api/events/{self.past_event.id}/'
#         self.client.force_authenticate(user=self.normal_user)
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_my_events_signup(self):
#         self.future_event.users.add(self.normal_user)
#         url = "/api/events/my"
#         self.client.force_authenticate(user=self.normal_user)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn(self.normal_user, self.future_event.users.all())