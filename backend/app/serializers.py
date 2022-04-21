from django.db.models import query
from rest_framework import serializers

from django.contrib.auth.models import User
from app.models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ["url", "title", "date", "status"]
