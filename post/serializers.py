from rest_framework import serializers
from social_network.models import SocialNetwork
from post.models import Post


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ["title", "description", "image", "scheduled_at", "social_networks"]


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "image_url",
            "social_networks",
            "created_at",
            "scheduled_at",
        ]
