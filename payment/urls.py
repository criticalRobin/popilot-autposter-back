from django.urls import path
from payment.views import CreateCheckoutSessionView

urlpatterns = [
    path(
        "create-checkout-session/",
        CreateCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
]
