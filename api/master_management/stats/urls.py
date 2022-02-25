from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
   path('stats/',
    views.StatsView.as_view(),
    name="stats_data"
   ),

   path('stats/<int:pk>/',
    views.StatsDetailView.as_view(),
    name="stats_data"
   )
]