from operator import mod
from pyexpat import model
from time import time
from django.db import models
from api.master_management.models import Season
from api.player_management.models import Player
from datetime import date
# Create your models here.


class Tournament(models.Model):
    tournament_name = models.CharField(
        max_length = 20,
        null = False,
        blank = False
    )
    season = models.ForeignKey(
        Season,
        related_name="Season",
        on_delete=models.DO_NOTHING,
    )
    tournament_type = models.CharField(
        max_length=10,
        default='',
        null=False,
        blank=False,
    )
    total_players = models.IntegerField(
        default=0,
        null=False,
        blank = False,
    )
    winner = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
        related_name="winner",
        null=True,
        blank=True,
    )
    runners_up = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
        related_name="runners_up",
        null=True,
        blank=True,
    )
    second_runners_up = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
        related_name="second_runners_up",
        null=True,
        blank=True,
    )
    top_Goal_Scorer = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
        related_name="top_goal_scorer",
        null=True,
        blank=True,
    )
    start_date = models.DateField(
        null=True,
        blank=False
    )
    end_date = models.DateField(
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f'{self.tournament_name}' + " " +f'{self.season.season}'