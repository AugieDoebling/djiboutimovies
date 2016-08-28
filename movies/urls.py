from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.genre_page),
    url(r'^(?P<genre>\w{0,15})/$', views.genre_page),
    url(r'^stream/([0-9]{0,6})/$', views.stream_page),
]