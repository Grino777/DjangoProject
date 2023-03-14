from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<int:id_movie>', views.get_movie_info, name='movie_detail'),
]