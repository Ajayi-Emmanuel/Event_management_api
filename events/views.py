from rest_framework import generics, permissions
from .models import Event
from .serializers import EventSerializer
from django.utils import timezone
from .filters import EventFilter
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response

from events import serializers

# List all events or create a new event
class EventListCreateView(generics.ListCreateAPIView):
    # get all events
    queryset = Event.objects.all()
    # use the EventSerializer class to serialize the data
    serializer_class = EventSerializer
    # set the permission class to allow only authenticated users to create events
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        # try to validate the serializer data and save the event if it is valid
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(organizer=self.request.user)
        # handle validation errors
        except serializers.ValidationError as e:
            # check if the error is due to a duplicate event title and date and time
            if 'title' in e.details and 'date_time' in e.details:
                return Response({'error': 'An event with this title and date and time already exists.',
                                 'isSuccess': False}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'error': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)     
            

# Retrieve, update or delete an event
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only the organizer of the event can update or delete it
        return self.queryset.filter(organizer=self.request.user)
    
# List all upcoming events
class UpcomingEventListView(generics.ListAPIView):
    # Filter the queryset to only include events that have not yet occurred
    queryset = Event.objects.filter(date_time__gte=timezone.now()).order_by('date_time')
    serializer_class = EventSerializer
    # Use the EventFilter class defined in filters.py
    filter_backends = [filters.DjangoFilterBackend]
    # Use the EventFilter class defined in filters.py
    filterset_class = EventFilter

