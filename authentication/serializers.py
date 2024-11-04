from rest_framework import serializers
from authentication.models import CustomUser


class LoggedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "is_premium_user",
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }
