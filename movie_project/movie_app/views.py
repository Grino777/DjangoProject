from django.shortcuts import render

def index(request):
    context = {
        'data': 'Ничего',
    }
    return render(request, 'movie_app/index.html', context=context)
