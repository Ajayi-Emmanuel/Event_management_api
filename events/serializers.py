from rest_framework import serializers
from .models import Event
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    # Read-only field that returns the username of the user who created the event
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        # Define the fields that should be serialized
        fields = ['id', 'title', 'description', 'date_time', 'location', 'organizer', 'capacity', 'created_date']

    # Validate that the event date and time is in the future
    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event date and time must be in the future.")
        return value
