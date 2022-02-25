from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
   path('seasondata/',
    views.SeasonView.as_view(),
    name="season_data"
   ),

   path('seasondata/<str:user_code>/',
    views.SeasonDetailView.as_view(),
    name="season_data"
   )
]