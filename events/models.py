from django.conf import settings
from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    # Define a foreign key field to associate the event with the user who created it
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    capacity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    # Define a many-to-many field to associate the event with the users who are attending it
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attended_events', blank=True)

    # Define a method to check if the event is full
    def is_full(self):
        # Return True if the number of attendees is greater than or equal to the capacity
        return self.attendees.count() >= self.capacity

    def __str__(self):
        return self.title
