# Common Imports
from rest_framework import serializers
from .models import (
    Stat
)


class StatsSerializers(serializers.ModelSerializer):
    class Meta:
        model =Stat
        fields = "__all__"
