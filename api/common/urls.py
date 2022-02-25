from django.urls import path, include


urlpatterns = [
    path(
        'media/',
        include("api.common.manage_media.urls"),
        name="media_urls"
    ),
]
