from django.urls import path
from social_network.views import (
    SocialNetworkListView,
    SocialNetworkCreateView,
    SocialNetworkUpdateView,
    SocialNetworkDeleteView,
)

urlpatterns = [
    path("list/", SocialNetworkListView.as_view(), name="social-network-list"),
    path("create/", SocialNetworkCreateView.as_view(), name="social-network-create"),
    path(
        "update/<int:pk>/",
        SocialNetworkUpdateView.as_view(),
        name="social-network-update",
    ),
    path(
        "delete/<int:pk>/",
        SocialNetworkDeleteView.as_view(),
        name="social-network-delete",
    ),
]
