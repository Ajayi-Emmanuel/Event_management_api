from rest_framework.permissions import BasePermission

# Define a custom permission class to check if the user is the organizer of the event
class IsOrganizer(BasePermission):
    # Define a method to check if the user has permission to perform the action
    def has_object_permission(self, request, view, obj):
        # Return True if the user is the organizer of the event
        return obj.organizer == request.user
