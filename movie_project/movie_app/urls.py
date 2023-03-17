from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.get_movie_info, name='movie_detail'),
    path('directors/<slug:slug_director>', views.get_info_about_director, name='director_info'),
    path('directors', views.show_all_directors),
]