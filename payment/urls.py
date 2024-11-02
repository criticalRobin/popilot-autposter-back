from django.urls import path
from payment.views import CreateCheckoutSessionView, UpdateUserIsPremiumStatusView

urlpatterns = [
    path(
        "create-checkout-session/",
        CreateCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path(
        "update-user-is-premium-status/",
        UpdateUserIsPremiumStatusView.as_view(),
        name="update-user-is-premium-status",
    ),
]
