from rest_framework import serializers
from social_network.models import FacebookAccount


class FacebookAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookAccount
        fields = [
            "id",
            "name",
            "social_network_type",
            "created_at",
            "status",
            "user_owner",
            "page_id",
            "page_access_token",
        ]
        read_only_fields = ["created_at", "user_owner"]
