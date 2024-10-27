import cloudinary.uploader


class Cloud:
    @staticmethod
    def upload(file):
        uploaded_image = cloudinary.uploader.upload(file)
        return uploaded_image.get("url")
