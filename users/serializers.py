# users/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # Add a password field to the serializer
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'email', 'is_staff', 'is_active'] # Add the password field to the fields list
        read_only_fields = ['is_staff', 'is_active'] # Set the is_staff and is_active fields to read-only


    def create(self, validated_data):
        # Hash the password before saving the user
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save() # Save the user
        return user
