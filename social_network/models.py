from django.db import models
from django.conf import settings


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
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.get_social_network_type_display()})"


class FacebookAccount(SocialNetwork):
    page_id = models.CharField(max_length=255)
    page_access_token = models.CharField(max_length=500)

    def __str__(self):
        return f"Facebook Page: {self.name} (ID: {self.page_id})"


class InstagramAccount(SocialNetwork):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"Instagram Account: {self.username}"


class XAccount(SocialNetwork):
    access_key = models.CharField(max_length=255)
    access_secret = models.CharField(max_length=255)
    consumer_key = models.CharField(max_length=255)
    consumer_secret = models.CharField(max_length=255)
    bearer_token = models.CharField(max_length=500)

    def __str__(self):
        return f"X (Twitter) Account: {self.name}"
