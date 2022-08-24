# Generated by Django 4.0.1 on 2022-08-23 20:21

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_ingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], max_length=50, null=True, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]
