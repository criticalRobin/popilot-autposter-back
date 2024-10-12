from social_network.serializers.serializers import SocialNetworkSerializer
from social_network.models import FacebookAccount


class FacebookAccountSerializer(SocialNetworkSerializer):
    class Meta(SocialNetworkSerializer.Meta):
        model = FacebookAccount
        fields = SocialNetworkSerializer.Meta.fields + ["page_id", "page_access_token"]
