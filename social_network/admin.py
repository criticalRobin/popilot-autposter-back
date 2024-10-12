from django.contrib import admin
from social_network.models import (
    SocialNetwork,
    FacebookAccount,
    InstagramAccount,
    XAccount,
)

# Register your models here.
admin.site.register(SocialNetwork)
admin.site.register(FacebookAccount)
admin.site.register(InstagramAccount)
admin.site.register(XAccount)
