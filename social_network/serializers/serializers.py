from rest_framework import serializers
from social_network.models import SocialNetwork


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = [
            "id",
            "name",
            "social_network_type",
            "created_at",
            "status",
            "user_owner",
        ]
        read_only_fields = ["id", "created_at"]
