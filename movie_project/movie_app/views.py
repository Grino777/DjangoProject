from django.db.models import Avg, Max, Min, Count, Value
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Movie, Director, Actor


# ---------- Movie CBV ----------
class MovieListView(ListView):
    template_name = 'movie_app/show_all_movie.html'
    model = Movie
    context_object_name = 'movies'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset)
    #     # agg = queryset.aggregate(Count('id'),
    #     #                            Avg('budget'),
    #     #                            Max('rating'),
    #     #                            Min('rating'),
    #     #                            )
    #     # queryset['agg'] = agg
    #     return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        agg = context['movies'].aggregate(Count('id'),
                                   Avg('budget'),
                                   Max('rating'),
                                   Min('rating'),
                                   )
        context['agg'] = agg
        return context

# def show_all_movie(request):
#     movies = Movie.objects.all()
#     movies = Movie.objects.annotate(new_field_bool=Value(True))
#     agg = movies.aggregate(Count('id'),
#                            Avg('budget'),
#                            Max('rating'),
#                            Min('rating'),
#                            )
#     context = {
#         'movies': movies,
#         'agg': agg,
#     }
#     return render(request, 'movie_app/show_all_movie.html', context=context)


class MovieDetailInfo(DetailView):
    template_name = 'movie_app/movie_info.html'
    model = Movie
    context_object_name = 'movie'


# def get_movie_info(request, slug_movie: str):
#     movie = get_object_or_404(Movie, slug=slug_movie)
#     context = {
#         'movie': movie,
#     }
#     return render(request, 'movie_app/movie_info.html', context=context)


# ---------- Movie CBV ----------

# ---------- Director CBV ----------
class DirectorListView(ListView):
    template_name = 'movie_app/directors.html'
    model = Director
    context_object_name = 'directors'


# def show_all_directors(request):
#     directors = Director.objects.all()
#     context = {
#         'directors': directors
#     }
#     return render(request, 'movie_app/directors.html', context=context)

class DirectorInfoView(DetailView):
    template_name = 'movie_app/director_info.html'
    model = Director
    context_object_name = 'director'


# def get_info_about_director(request, slug_director):
#     director = get_object_or_404(Director, slug=slug_director)
#     context = {
#         'director': director,
#     }
#     return render(request, 'movie_app/director_info.html', context=context)
# ---------- Director CBV ----------

# ---------- Actor CBV ----------
class ActorsListView(ListView):
    template_name = 'movie_app/actors.html'
    model = Actor
    context_object_name = 'actors'


# def show_all_actors(request):
#     actors = Actor.objects.all()
#     context = {
#         'actors': actors
#     }
#     return render(request, 'movie_app/actors.html', context=context)

class ActorInfoView(DetailView):
    template_name = 'movie_app/actor_info.html'
    model = Actor
    context_object_name = 'actor'

# def get_info_about_actor(request, slug_actor):
#     actor = get_object_or_404(Actor, slug=slug_actor)
#     context = {
#         'actor': actor,
#     }
#     return render(request, 'movie_app/actor_info.html', context=context)
# ---------- Actor CBV ----------
