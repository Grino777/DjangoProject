from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from slugify import slugify

def instance_slug(instance):
    return instance.slug

def slugify_value(value:str):
    return value.replace(' ', '-')


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Жещина')
    ]

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    gender = models.CharField(choices=GENDERS, max_length=1, default=MALE, verbose_name='Пол')
    # slug = models.SlugField(blank=True, db_index=True, null=False, unique=True)
    slug = AutoSlugField('SLUG', max_length=100, db_index=True,
                         unique=True, populate_from=instance_slug, slugify=slugify_value)


    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        return f'Актриса {self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name} {self.last_name}')
        super(Actor, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('actor_info', args=(self.slug,))


class Director(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(blank=True, verbose_name='Почта')
    slug = AutoSlugField('slug', max_length=100, db_index=True,
                         unique=True, populate_from=instance_slug, slugify=slugify_value)
    # slug = models.SlugField(null=False, db_index=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('director_info', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name} {self.last_name}')
        super(Director, self).save(*args, **kwargs)


class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRNECY_CHOICES = [
        (RUB, 'Rubles'),
        (USD, 'Dollars'),
        (EURO, 'Euro'),
    ]

    name = models.CharField(max_length=40, verbose_name='Название фильма')
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)], verbose_name='Рейтинг')
    year = models.IntegerField(null=True, blank=True, verbose_name='Год')
    budget = models.IntegerField(default=1000000, validators=[MinValueValidator(1)], verbose_name='Бюджет')
    currency = models.CharField(max_length=3, choices=CURRNECY_CHOICES, default=RUB, verbose_name='Валюта')
    directors = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Режисер') #related_name - атрибут для изменения названия доступа к связным таблицам
    actors = models.ManyToManyField(Actor, blank=True, verbose_name='Актеры')
    # slug = models.SlugField(default='', null=False)
    slug = AutoSlugField('SLUG', max_length=100, db_index=True,
                         unique=True, populate_from=instance_slug, slugify=slugify_value)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f"{self.name} - {self.rating}"