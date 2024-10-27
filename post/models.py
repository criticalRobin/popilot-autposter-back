from django.db import models
from django.conf import settings
from social_network.models import SocialNetwork


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True, null=True)
    social_networks = models.ManyToManyField(SocialNetwork, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return
