from django.urls import path
from post.views import PostCreateView, PostNoScheduledListView, PostScheduledListView

urlpatterns = [
    path("list/", PostNoScheduledListView.as_view(), name="post_list"),
    path(
        "list/scheduled/", PostScheduledListView.as_view(), name="post_list_scheduled"
    ),
    path("create/", PostCreateView.as_view(), name="post_create"),
]
