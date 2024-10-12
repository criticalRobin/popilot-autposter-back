from social_network.models import XAccount
from rest_framework import serializers


class XAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = XAccount
        fields = [
            "id",
            "name",
            "social_network_type",
            "created_at",
            "status",
            "user_owner",
            "access_key",
            "access_secret",
            "consumer_key",
            "consumer_secret",
            "bearer_token",
        ]
        read_only_fields = ["created_at", "user_owner"]
