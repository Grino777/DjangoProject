# Generated by Django 4.1.7 on 2023-03-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0011_director_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(),
        ),
    ]
