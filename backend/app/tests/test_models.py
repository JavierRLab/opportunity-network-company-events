from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .. import models


# Create your tests here.
class ModelTests(TestCase):
    def test_event_title_str(self):
        """Test the Event string representation"""
        event = models.Event.objects.create(title="my first event")

        self.assertEqual(str(event), event.title)
