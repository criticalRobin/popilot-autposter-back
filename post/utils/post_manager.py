import requests
from io import BytesIO
from social_network.models import XAccount, FacebookAccount, InstagramAccount
import tweepy
from instagrapi import Client
from PIL import Image
import tempfile


class PostManager:
    def post_on_x_account(self, x_account: XAccount, image_url, description):
        auth = tweepy.OAuthHandler(x_account.consumer_key, x_account.consumer_secret)
        auth.set_access_token(x_account.access_key, x_account.access_secret)

        new_api = tweepy.Client(
            bearer_token=x_account.bearer_token,
            access_token=x_account.access_key,
            access_token_secret=x_account.access_secret,
            consumer_key=x_account.consumer_key,
            consumer_secret=x_account.consumer_secret,
        )

        api = tweepy.API(auth)

        response = requests.get(image_url)
        if response.status_code == 200:
            image_file = BytesIO(response.content)
            media = api.media_upload(filename="image.jpg", file=image_file)
            post_result = new_api.create_tweet(
                text=description, media_ids=[media.media_id]
            )

            return post_result
        else:
            return None

    def post_on_facebook_account(
        self, facebook_account: FacebookAccount, image_url, description
    ):
        url = f"https://graph.facebook.com/v21.0/{facebook_account.page_id}/photos"
        params = {
            "access_token": facebook_account.page_access_token,
            "message": description,
            "url": image_url,
        }

        try:
            response = requests.post(url, data=params)
            result = response.json()

            if "id" in result:
                return "Post created successfully"
            else:
                return result
        except Exception as e:
            return str(e)

    def post_on_instagram_account(
        self, instagram_account: InstagramAccount, image_url, description
    ):
        cl = Client()
        cl.login(instagram_account.username, instagram_account.password)

        response = requests.get(image_url)

        if response.status_code == 200:
            image_file = BytesIO(response.content)

            img = Image.open(image_file)

            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                img.save(temp_file, format="JPEG")
                temp_file_path = temp_file.name

            cl.photo_upload(temp_file_path, description)

            return "Post created successfully"
