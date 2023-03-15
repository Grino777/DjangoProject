from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Avg, Max, Min, Sum, Count

def show_all_movie(request):
    movies = Movie.objects.all()
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