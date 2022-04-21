from django.db import models
from django.utils import timezone


class Event(models.Model):
    """Table schema to store Events."""

    class Status(models.TextChoices):
        DRAFT = "DR"
        PRIVATE = "PR"
        PUBLIC = "PU"

    # user_organizing
    # users_subscribed
    title = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    def __str__(self):
        return self.title
