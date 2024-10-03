from django.db import models
from django.contrib.auth.models import AbstractUser

# Define a custom User model that extends the AbstractUser class which provides the default fields and methods for the User model
class User(AbstractUser):
    # Define custom fields for the User model
    groups = models.ManyToManyField('auth.Group', related_name='users', related_query_name='user')
    # Define a many-to-many field to associate the user with permissions
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users', related_query_name='user')
    password = models.CharField(max_length=128) # Override the password field to increase the max length

