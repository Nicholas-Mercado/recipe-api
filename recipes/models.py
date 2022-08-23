from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    recipe = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.recipe
