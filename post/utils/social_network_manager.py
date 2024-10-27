from social_network.models import SocialNetwork


class SocialNetworkManager:
    @staticmethod
    def get_social_networks(social_networks_id_array):
        social_networks = []

        for sn in social_networks_id_array:
            social_network = SocialNetwork.objects.select_subclasses().get(id=sn)
            social_networks.append(social_network)

        return social_networks
