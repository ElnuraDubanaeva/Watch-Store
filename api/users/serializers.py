from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(
        max_length=30,
        min_length=2,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        max_length=20,
        min_length=6,
        validators=[validate_password],
        style={"input_type": "password"},
        write_only=True,
    )


class LoginSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
