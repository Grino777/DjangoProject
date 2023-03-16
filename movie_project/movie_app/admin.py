from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet

# Register your models here.

@admin.register(Movie) #Регистрация БД в админке для ее дальнейшего отображения
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget','rating_status'] #Отображаемые поля в админке
    list_editable = ['currency', 'rating'] #Изменяемые поля
    ordering = ['-rating', 'name'] #Фильтрация полей по заданным колонкам при отображении их в админке
    list_per_page = 20 #Пагинация
    actions = ['set_dollars', 'set_euro'] #Отображение действий с записями в админке
    search_fields = ['name', ] #Поле поиска (нечувстительное к регистру sqlite)

    @admin.display(ordering='rating', description='Статус') #Отображение вспомогательных колонок в админке
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть?'
        if movie.rating < 70:
            return 'На разок'
        if movie.rating <=85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в долларах') #Регистрация действий в админке
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.EURO)
        self.message_user(request, message=f'Было обновлено {count_updated} записей') #Вывод информационного поля для пользователя