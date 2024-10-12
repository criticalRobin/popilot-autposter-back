from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from social_network.models import (
    SocialNetwork,
    FacebookAccount,
    InstagramAccount,
    XAccount,
)
from social_network.serializers.facebook_acount.serializers import (
    FacebookAccountSerializer,
)
from social_network.serializers.instagram_account.serializers import (
    InstagramAccountSerializer,
)
from social_network.serializers.x_account.serializers import XAccountSerializer
from rest_framework.response import Response


class SocialNetworkListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        facebook_accounts = FacebookAccount.objects.filter(user_owner=user, status=True)
        instagram_accounts = InstagramAccount.objects.filter(
            user_owner=user, status=True
        )
        x_accounts = XAccount.objects.filter(user_owner=user, status=True)

        data = {
            "facebook_accounts": FacebookAccountSerializer(
                facebook_accounts, many=True
            ).data,
            "instagram_accounts": InstagramAccountSerializer(
                instagram_accounts, many=True
            ).data,
            "x_accounts": XAccountSerializer(x_accounts, many=True).data,
        }

        return Response(data)


class SocialNetworkCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        social_network_type = data.get("social_network_type")

        if social_network_type == "FB":
            return self._create_social_account(
                FacebookAccountSerializer, FacebookAccount, data, user
            )
        elif social_network_type == "IG":
            return self._create_social_account(
                InstagramAccountSerializer, InstagramAccount, data, user
            )
        elif social_network_type == "X":
            return self._create_social_account(XAccountSerializer, XAccount, data, user)
        else:
            return Response(
                {"error": "Invalid social network type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def _create_social_account(self, serializer_class, model_class, data, user):
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            model_class.objects.create(user_owner=user, **serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialNetworkUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = request.user
        data = request.data
        social_network_type = data.get("social_network_type")

        if social_network_type == "FB":
            return self._update_social_account(
                FacebookAccountSerializer, FacebookAccount, data, user, pk
            )
        elif social_network_type == "IG":
            return self._update_social_account(
                InstagramAccountSerializer, InstagramAccount, data, user, pk
            )
        elif social_network_type == "X":
            return self._update_social_account(
                XAccountSerializer, XAccount, data, user, pk
            )
        else:
            return Response(
                {"error": "Invalid social network type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def _update_social_account(self, serializer_class, model_class, data, user, pk):
        try:
            social_account = model_class.objects.get(user_owner=user, pk=pk)
        except model_class.DoesNotExist:
            return Response(
                {"error": "Social account not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = serializer_class(social_account, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialNetworkDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        user = request.user
        social_network_type = SocialNetwork.objects.get(pk=pk).social_network_type

        if social_network_type == "FB":
            return self._delete_social_account(FacebookAccount, user, pk)
        elif social_network_type == "IG":
            return self._delete_social_account(InstagramAccount, user, pk)
        elif social_network_type == "X":
            return self._delete_social_account(XAccount, user, pk)
        else:
            return Response(
                {"error": "Invalid social network type"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def _delete_social_account(self, model_class, user, pk):
        try:
            social_account = model_class.objects.get(user_owner=user, pk=pk)
        except model_class.DoesNotExist:
            return Response(
                {"error": "Social account not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        social_account.status = False
        social_account.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
