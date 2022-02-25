from django.db import models

# Create your models here.
class Season(models.Model):
    season=models.CharField(
        max_length=9,
        null=False,
        blank=False
    )
    is_active=models.BooleanField(
        null=False,
        blank=False
    )
    
    def __str__(self):
        return "("+f'{self.season}'+")"