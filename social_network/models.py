from django.db import models
from django.conf import settings
from model_utils.managers import InheritanceManager


class SocialNetwork(models.Model):
    SOCIAL_NETWORK_CHOICES = [
        ("FB", "Facebook"),
        ("IG", "Instagram"),
        ("X", "X (Twitter)"),
    ]
    name = models.CharField(max_length=100)
    social_network_type = models.CharField(
        max_length=2, choices=SOCIAL_NETWORK_CHOICES, default="IG"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = InheritanceManager()

    def __str__(self):
        return f"{self.id}"


class FacebookAccount(SocialNetwork):
    page_id = models.CharField(max_length=255)
    page_access_token = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}"


class InstagramAccount(SocialNetwork):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}"


class XAccount(SocialNetwork):
    access_key = models.CharField(max_length=255)
    access_secret = models.CharField(max_length=255)
    consumer_key = models.CharField(max_length=255)
    consumer_secret = models.CharField(max_length=255)
    bearer_token = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}"
