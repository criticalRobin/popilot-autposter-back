from social_network.serializers.serializers import SocialNetworkSerializer
from social_network.models import InstagramAccount


class InstagramAccountSerializer(SocialNetworkSerializer):
    class Meta(SocialNetworkSerializer.Meta):
        model = InstagramAccount
        fields = SocialNetworkSerializer.Meta.fields + ["username", "password"]
