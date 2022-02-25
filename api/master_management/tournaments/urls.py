from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
   path('tournamentdata/',
    views.TournamentView.as_view(),
    name="season_data"
   ),

   path('tournamentdata/<int:pk>/',
    views.TournamentDetailView.as_view(),
    name="season_data"
   )
]