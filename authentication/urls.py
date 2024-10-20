from django.urls import path
from authentication.views import LoggedUserView

urlpatterns = [
    path("logged-user/", LoggedUserView.as_view(), name="logged-user"),
]
