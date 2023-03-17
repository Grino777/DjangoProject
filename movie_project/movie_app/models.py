from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
# from transliterate import translit

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('director_info', args=(self.slug,))

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(translit(str(self), 'ru', reversed=True))
    #     super(Director, self).save(*args, **kwargs)


class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRNECY_CHOICES = [
        (RUB, 'Rubles'),
        (USD, 'Dollars'),
        (EURO, 'Euro'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRNECY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False)
    directors = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"
