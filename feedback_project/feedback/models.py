from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=75, validators=[MaxLengthValidator(75)])
    surname = models.CharField(max_length=75, validators=[MaxLengthValidator(75)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
