from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

USER = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = USER
        fields = ('id', 'email', 'name', 'password')


class PasswordChangeSerializer(serializers.Serializer):
    """
    Name: Password Change Serializer
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
