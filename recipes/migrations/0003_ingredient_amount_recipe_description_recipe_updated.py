# Generated by Django 4.0.1 on 2022-08-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient_recipe_url_recipe_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
