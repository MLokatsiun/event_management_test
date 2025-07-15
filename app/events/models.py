from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """
    Represents an event organized by a user.

    Fields:
    - title: The name/title of the event.
    - description: Detailed description of the event.
    - date: The scheduled date and time of the event.
    - location: The place where the event will take place.
    - organizer: The user who created/organizes the event.

    The __str__ method returns the event's title for easy identification.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    """
    Represents the registration of a user to an event.

    Fields:
    - user: The user who registered for the event.
    - event: The event the user registered for.
    - registered_at: Timestamp when the registration was created (auto-set on creation).

    The Meta option `unique_together` ensures a user cannot register multiple times for the same event.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
