from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='all_movies'),
    path('movie/<slug:slug>', views.MovieDetailInfo.as_view(), name='movie_detail'),
    path('director/<slug:slug>', views.DirectorInfoView.as_view(), name='director_info'),
    path('directors', views.DirectorListView.as_view(), name='all_directors'),
    path('actors', views.ActorsListView.as_view(), name='all_actors'),
    path('actor/<slug:slug>', views.ActorInfoView.as_view(), name='actor_info'),
]