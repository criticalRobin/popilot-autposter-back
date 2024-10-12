from social_network.serializers.serializers import SocialNetworkSerializer
from social_network.models import XAccount


class XAccountSerializer(SocialNetworkSerializer):
    class Meta(SocialNetworkSerializer.Meta):
        model = XAccount
        fields = SocialNetworkSerializer.Meta.fields + [
            "access_key",
            "access_secret",
            "consumer_key",
            "consumer_secret",
            "bearer_token",
        ]
