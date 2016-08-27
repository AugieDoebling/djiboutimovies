from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.genre_page),
    url(r'^([0-9]{4})/$', views.genre_page),
]