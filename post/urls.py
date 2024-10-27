from django.urls import path
from post.views import PostCreateView

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="post_create"),
]
