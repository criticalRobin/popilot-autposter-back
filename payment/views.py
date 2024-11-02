import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(APIView):
    def post(self, request):
        try:
            items = request.data.get("items", [])
            success_url = request.data.get("successURL")
            cancel_url = request.data.get("cancelURL")

            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=items,
                mode="payment",
                success_url=success_url,
                cancel_url=cancel_url,
            )
            return Response({"sessionId": session.id})
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateUserIsPremiumStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            user.is_premium_user = True
            user.save()
            return Response({"message": "User is now premium"})
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
