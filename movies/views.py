from django.shortcuts import get_object_or_404, render

from .models import Movie

def movie_page(request):
    movie_list = Movie.objects.order_by('title')
    context = {'movie_list' : movie_list}
    return render(request, 'movies/index.html', context)


# def movie_page(request, genre):
#     movie_list = Movie.objects.order_by('title')
#     context = {'movie_list' : movie_list, "genre" : genre}
#     return render(request, 'movies/index.html', context)