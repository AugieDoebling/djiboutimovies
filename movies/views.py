from django.shortcuts import get_object_or_404, render

from .models import Movie

def movie_page(request):
    movie_list = Movie.objects.order_by('title')
    context = {'movie_list' : movie_list}
    return render(request, 'movies/index.html', context)


def genre_page(request, genre=None):
    movie_list = Movie.objects.order_by('title')
    context = {'movie_list' : movie_list, "genre" : genre}
    return render(request, 'movies/index.html', context)

def stream_page(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/watch.html', context)

