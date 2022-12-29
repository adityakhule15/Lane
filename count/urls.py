from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('home/', views.home, name="home"),
        path('like/', views.like, name="like"),
        path('dislike/', views.dslike, name="dislike"),
]