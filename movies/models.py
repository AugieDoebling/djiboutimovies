from __future__ import unicode_literals
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    running_time_min = models.IntegerField(default=0)
    genre_one = models.CharField(max_length=200)
    genre_two = models.CharField(max_length=200)
    genre_three = models.CharField(max_length=200)
    imdb_rating = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, unique=False)
    img_url = models.CharField(max_length=200)
    file_url = models.CharField(max_length=200)

    def __cmp__(self, other):
        return self.title.__cmp__(other.title)
