from rest_framework import serializers
from .models import Thing


class Recipeserializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = "__all__"
