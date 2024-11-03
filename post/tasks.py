from celery import shared_task
from post.utils.post_manager import PostManager
from post.models import Post
from social_network.models import (
    SocialNetwork,
    FacebookAccount,
    InstagramAccount,
    XAccount,
)
import logging
from post.utils.social_network_manager import SocialNetworkManager as snm

logger = logging.getLogger(__name__)


@shared_task
def publish_post(post_id):
    try:
        post = Post.objects.get(id=post_id)
        social_network_ids = [
            sn.id for sn in post.social_networks.all()
        ] 
        social_networks = snm.get_social_networks(social_network_ids)

        for sn in social_networks:
            if isinstance(sn, FacebookAccount):
                PostManager().post_on_facebook_account(
                    sn, post.image_url, post.description
                )
            elif isinstance(sn, InstagramAccount):
                PostManager().post_on_instagram_account(
                    sn, post.image_url, post.description
                )
            elif isinstance(sn, XAccount):
                PostManager().post_on_x_account(sn, post.image_url, post.description)

        post.posted = True
        post.save()
    except Post.DoesNotExist:
        print(f"Post no encontrado con ID: {post_id}")
    except Exception as e:
        print(f"Error al publicar el post: {str(e)}")
