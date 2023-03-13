from django.shortcuts import render
from django.db import connection
from models import Movie

# Create your views here.

def index(request):
    context = {
        'data': connection.queries,
        'movies': Movie.objects.all(),
    }
    return render(request, 'movie_app/index.html', context=context)