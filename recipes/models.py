from django.contrib.auth import get_user_model
from django.db import models
from .validators import validate_unit_of_measure, MEASUREMENT_CHOICES



class Ingredient(models.Model):
    """ Creates a ingredient model with name, amount, and units"""
    name = models.CharField(max_length=30)
    amount = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure], choices=MEASUREMENT_CHOICES, blank=True, null=True)
    def __str__(self):
        return f"{self.amount}, {self.unit}, {self.name}"


class Recipe(models.Model):

    """ Creates a recipe model with name, url, description, and linked to ingredients"""
    recipe = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200, null=True,blank=True)
    ingredient = models.ManyToManyField(Ingredient)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.recipe
