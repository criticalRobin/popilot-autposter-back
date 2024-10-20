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
