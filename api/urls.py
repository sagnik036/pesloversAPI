from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    
    path(
        'players/',
        include('api.player_management.urls'),
        name='players_management'
    ),

    path(
        'mastermanagement/',
        include('api.master_management.urls'),
        name='master_management'
    ),

    
]