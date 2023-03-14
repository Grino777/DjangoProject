from django.shortcuts import render, get_object_or_404
from .models import Movie

def show_all_movie(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie_app/show_all_movie.html', context=context)

def get_movie_info(request, id_movie: int):
    movie = get_object_or_404(Movie, id=id_movie)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_app/movie_info.html', context=context)