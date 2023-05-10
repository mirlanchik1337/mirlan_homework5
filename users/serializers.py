from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError


class UserAuthorizeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateSerializer(UserAuthorizeSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User is already exist!')