from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
   path('playerdata/',
    views.PlayerView.as_view(),
    name="player"
   ),

   path('playerdata/<int:pk>/',
    views.PlayerDetailView.as_view(),
    name="player"
   )
]