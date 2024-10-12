from social_network.models import InstagramAccount
from rest_framework import serializers


class InstagramAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramAccount
        fields = [
            "id",
            "name",
            "social_network_type",
            "created_at",
            "status",
            "user_owner",
            "username",
            "password",
        ]
        read_only_fields = ["created_at", "user_owner"]
