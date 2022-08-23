from django.contrib.auth import get_user_model
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name


class Recipe(models.Model):

    """ Creates a recipe model with recipe_name, url, and linked to ingredients"""
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
