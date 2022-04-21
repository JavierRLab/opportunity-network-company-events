from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


EVENTS_URL = "/events/"
# Create your tests here.
class EndpointTests(TestCase):
    """Test the API"""

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test", email="test@email.com", password="password"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_events_url(self):
        """Test for retrieving all events"""
        res = self.client.get(EVENTS_URL)
        print(res)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
