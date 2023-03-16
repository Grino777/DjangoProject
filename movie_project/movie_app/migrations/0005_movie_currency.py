# Generated by Django 4.1.7 on 2023-03-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('R', 'Rubles'), ('D', 'Dollars'), ('E', 'Euro')], default='R', max_length=1),
        ),
    ]
