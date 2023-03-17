from django.shortcuts import render, get_object_or_404
from .models import Movie, Director
from django.db.models import F, Avg, Max, Min, Sum, Count, Value

def show_all_movie(request):
    movies = Movie.objects.all()
    movies = Movie.objects.annotate(new_field_bool=Value(True))
    agg = movies.aggregate(Count('id'),
                           Avg('budget'),
                           Max('rating'),
                           Min('rating'),
                           )
    context = {
        'movies': movies,
        'agg': agg,
    }
    return render(request, 'movie_app/show_all_movie.html', context=context)

def get_movie_info(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_app/movie_info.html', context=context)

def show_all_directors(request):
    directors = Director.objects.all()
    for i in directors:
        i.save()
        print(i.slug)
    context = {
        'directors': directors
    }
    return render(request, 'movie_app/directors.html', context=context)

def get_info_about_director(request, slug_director):
    director = get_object_or_404(Director, slug=slug_director)
    context = {
        'director': director,
    }
    return render(request, 'movie_app/director_info.html', context=context)