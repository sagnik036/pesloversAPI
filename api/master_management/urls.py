from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
     path(
         'seasons/',
         include('api.master_management.seasons.urls'),
         name='seasons'
     ),
     path(
         'tournaments/',
         include('api.master_management.tournaments.urls'),
         name='tournament'
     ),
     path(
         'statistics/',
         include('api.master_management.stats.urls'),
         name='statistics'
     )

]