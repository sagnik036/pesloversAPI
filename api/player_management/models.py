from django.db import models
import random
# Create your models here.
class Player(models.Model):
    user_code = models.CharField(
        max_length=15,
        unique=True,
        editable=False,
        null=False,
        blank=False
    )
    name=models.CharField(
        max_length=15,
        null=False,
        blank=False
    )
    pes_id=models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False
    )
    whats_app=models.CharField(
        max_length=10,
        unique=True,  
        null=False,
        blank=False
    )
    team_photo=models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    
    def save(self,*args, **kwargs):
        if (not self.id):
         self.user_code = f'{self.name[0:4].upper()}' + f'{random.randrange(34, 916)}'+f'{random.randrange(125, 965)}'
         super(Player, self).save(*args, **kwargs)
        else:
          super(Player, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.name}' +' | UserCode : '+ f'{self.user_code}'