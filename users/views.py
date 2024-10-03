# users/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer

# generics are used to create views that perform CRUD operations on models without having to write the same code repeatedly

# Define a view to list and create users
class UserListView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# Define a view to retrieve, update and delete users
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
