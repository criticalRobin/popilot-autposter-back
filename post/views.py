from rest_framework.views import APIView
from post.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from post.utils.cloud import Cloud as cloud
from post.utils.social_network_manager import SocialNetworkManager as snm
from post.utils.post_manager import PostManager
from social_network.models import FacebookAccount, InstagramAccount, XAccount
from post.models import Post


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            social_networks_id_array = request.data.getlist("social_networks")
            social_networks = snm.get_social_networks(social_networks_id_array)
            title = request.data.get("title")
            description = request.data.get("description")
            scheduled_at = request.data.get("scheduled_at")
            image = request.FILES.get("image")

            image_url = cloud.upload(image) if image else None

            post = Post.objects.create(
                title=title,
                user=request.user,
                description=description,
                image_url=image_url,
                scheduled_at=scheduled_at,
            )

            post.social_networks.set(social_networks)

            for sn in social_networks:
                if isinstance(sn, FacebookAccount):
                    PostManager().post_on_facebook_account(sn, image_url, description)
                elif isinstance(sn, InstagramAccount):
                    PostManager().post_on_instagram_account(sn, image_url, description)
                elif isinstance(sn, XAccount):
                    PostManager().post_on_x_account(sn, image_url, description)

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
