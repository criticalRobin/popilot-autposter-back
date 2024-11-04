from django.urls import path
from authentication.views import LoggedUserView, CreateUserView

urlpatterns = [
    path("logged-user/", LoggedUserView.as_view(), name="logged-user"),
    path("create-user/", CreateUserView.as_view(), name="create-user"),
]
