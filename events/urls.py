from django.urls import path
from .views import EventListCreateView, EventDetailView, UpcomingEventListView

urlpatterns = [
    # url for creating and listing events
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # url for viewing, updating and deleting an event
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    # url for listing upcoming events based on the date
    path('events/upcoming/', UpcomingEventListView.as_view(), name='upcoming-event-list'),
]
