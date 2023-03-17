from django.contrib import admin
from django.db.models import QuerySet

from .models import Movie, Director


# Register your models here.

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'  # Отображаемое название фильтра
    parameter_name = 'rating'  # Параметр который подставляется в url

    def lookups(self, request,
                model_admin):  # Обязательный для переопределения метод. Возвращает отоброжаемые данные List[tuple]
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 59 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request,
                 queryset: QuerySet):  # Второй обяательный к переопределению метод. Возвращает отфильтрованный qeryset
        # У self имеется метод value (self.value()) который принимает входящий параметр с фильтра
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lte=59)
        if self.value() == 'от 59 до 79':
            return queryset.filter(rating__gte=59).filter(rating__lt=79)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)

        return queryset

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'slug']
    prepopulated_fields = {'slug': ('first_name', 'last_name'),}

@admin.register(Movie)  # Регистрация БД в админке для ее дальнейшего отображения
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating', 'year', 'currency', 'budget',] #Отображение полей в форме редактирования/создания записи
    #exclude = ['slug']  # Исключает поля в форме редактирования/создания записи
    prepopulated_fields = {'slug': ('name',),} #Предвычисляемое поле
    list_display = ['name', 'rating', 'directors', 'budget', 'rating_status']  # Отображаемые поля в админке
    list_editable = ['directors', 'rating']  # Изменяемые поля
    ordering = ['-rating', 'name']  # Фильтрация полей по заданным колонкам при отображении их в админке
    #readonly_fields = ['slug']  # Поля только для чтения
    #list_per_page = 20  # Пагинация
    actions = ['set_dollars', 'set_euro']  # Отображение действий с записями в админке
    search_fields = ['name', ]  # Поле поиска (нечувстительное к регистру sqlite)
    list_filter = [RatingFilter]

    @admin.display(ordering='rating', description='Статус')  # Отображение вспомогательных колонок в админке
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть?'
        if movie.rating < 70:
            return 'На разок'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в долларах')  # Регистрация действий в админке
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.EURO)
        self.message_user(request,
                          message=f'Было обновлено {count_updated} записей')  # Вывод информационного поля для пользователя
