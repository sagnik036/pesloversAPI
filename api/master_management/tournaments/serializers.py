# Common Imports
from rest_framework import serializers
from .models import (
    Tournament
)


class TournamentSerializers(serializers.ModelSerializer):
    class Meta:
        model =Tournament
        fields = "__all__"
