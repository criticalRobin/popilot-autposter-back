from django.urls import path
from post.views import PostCreateView, PostListView

urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
]
