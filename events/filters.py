from django_filters import rest_framework as filters
from .models import Event

# Define a filter class for the Event model
class EventFilter(filters.FilterSet):
    # Define the filter fields and the lookup expressions to use for filtering
    # The lookup expressions are used to filter the queryset based on the filter fields
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = filters.CharFilter(field_name='location', lookup_expr='icontains')
    date_range = filters.DateTimeFromToRangeFilter(field_name='date_time', lookup_expr='range')

    class Meta:
        model = Event
        # Define the fields that can be used to filter the queryset
        fields = ['title', 'location', 'date_time']
