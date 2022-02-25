from django.db import models
from api.player_management.models import Player
from api.master_management.tournaments.models import Tournament

# Create your models here.
class Stat(models.Model):
    player_name = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING
    )
    tournament  = models.ForeignKey(
        Tournament,
        on_delete=models.DO_NOTHING
    )
    goals = models.IntegerField()

    def __str__(self):
        return f'{self.player_name.name}' + ":" + f'{self.player_name.user_code}'