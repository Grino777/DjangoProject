# Generated by Django 4.1.7 on 2023-03-22 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(5)])),
                ('surname', models.CharField(max_length=75)),
                ('feedback', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]
