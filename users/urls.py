# users/urls.py
from django.urls import path
from .views import UserListView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Define the login URL path using the TokenObtainPairView view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Define the token refresh URL path using the TokenRefreshView view
    path('users/', UserListView.as_view(), name='user-list'), # the url to list and create a user
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), # the url to view, update and delete a user
]
    