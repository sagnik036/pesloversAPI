from django.views import View
# Cloudinary Imports
import cloudinary
import cloudinary.uploader
from django.conf import settings

cloudinary.config(
  cloud_name=settings.CLOUD_NAME,
  api_key=settings.CLOUDINARY_KEY,
  api_secret=settings.CLOUDINARY_SECRETS,
  secure=True
)


class MediaUploadServices(View):
    @staticmethod
    def upload_to_cloudinary(file, upload_path=settings.DEFAULT_UPLOAD_PATH):
        upload_response = cloudinary.uploader.upload(
            file,
            folder=upload_path
        )
        result = upload_response.get("url")
        return result
