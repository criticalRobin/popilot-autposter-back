from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subscription.serializers import CardInformationSerializer
import stripe


class PaymentAPI(APIView):
    serializer_class = CardInformationSerializer

    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        response = {}

        if serializer.is_valid():
            data_dict = serializer.validated_data
            stripe.api_key = "your-key-goes-here"
            response = self.stripe_card_payment(data_dict)

            return Response(
                response, status=response.get("status", status.HTTP_400_BAD_REQUEST)
            )

        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

    def stripe_card_payment(self, data_dict):
        try:
            card_details = {
                "number": data_dict["card_number"],
                "exp_month": data_dict["expiry_month"],
                "exp_year": data_dict["expiry_year"],
                "cvc": data_dict["cvc"],
            }

            payment_intent = stripe.PaymentIntent.create(
                    amount=10,
                currency="inr",
                payment_method_data={
                    "type": "card",
                    "card": card_details,
                },
            )

            payment_confirm = stripe.PaymentIntent.confirm(payment_intent["id"])

            if payment_confirm["status"] == "succeeded":
                response = {
                    "message": "Card Payment Success",
                    "status": status.HTTP_200_OK,
                    "payment_intent": payment_confirm,
                }
            else:
                response = {
                    "message": "Card Payment Failed",
                    "status": status.HTTP_400_BAD_REQUEST,
                    "payment_intent": payment_confirm,
                }

        except stripe.error.CardError as e:
            response = {
                "error": str(e),
                "status": status.HTTP_400_BAD_REQUEST,
            }
        except Exception as e:
            response = {
                "error": str(e),
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            }

        return response
