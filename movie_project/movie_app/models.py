from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


# from transliterate import translit

class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Жещина')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDERS, max_length=1, default=MALE)
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        return f'Актриса {self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('actor_info', args=(self.slug,))


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
    actors = models.ManyToManyField(Actor, blank=True)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"
