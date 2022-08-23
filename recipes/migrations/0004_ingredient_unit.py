# Generated by Django 4.0.1 on 2022-08-23 19:49

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredient_amount_recipe_description_recipe_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]
