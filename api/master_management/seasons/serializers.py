# Common Imports
from rest_framework import serializers
from .models import (
    Season
)


class SeasonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"
