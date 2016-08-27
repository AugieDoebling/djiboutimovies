from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.genre_page),
    url(r'^(?P<genre>\w{0,15})/$', views.genre_page),
]