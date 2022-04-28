from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^musics/$', views.Musiclist.as_view(), name='music-list'),
  
]