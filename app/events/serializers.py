from rest_framework import serializers
from .models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.

    Serializes all fields of the Event model.

    The 'organizer' field is read-only and cannot be set or modified by clients,
    since it is assigned automatically based on the authenticated user creating the event.
    """
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('organizer',)


class EventRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for the EventRegistration model.

    Serializes all fields of the EventRegistration model.

    The 'user' field is read-only and is automatically set to the authenticated user
    who registers for an event.
    """
    class Meta:
        model = EventRegistration
        fields = '__all__'
        read_only_fields = ('user',)
