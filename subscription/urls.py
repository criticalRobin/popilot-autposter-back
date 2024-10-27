from django.urls import path
from subscription.views import PaymentAPI

urlpatterns = [path("make_payment/", PaymentAPI.as_view(), name="make_payment")]
