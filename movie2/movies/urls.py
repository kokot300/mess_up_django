"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import add_genre, add_movie, all_movies, movie_details, edit_movie, search_movie, delete_movie

urlpatterns = [
    path('add_genre/', add_genre, name='add-genre'),
    path('add_movie/', add_movie, name='add-movie'),
    path('', all_movies, name='movie-list'),
    path('<int:movie_id>/detail/', movie_details, name='movie-details'),
    path('<int:movie_id>/edit/', edit_movie, name='edit-movie'),
    path('search/', search_movie, name='search-movie'),
    path('<int:movie_id>/delete/', delete_movie, name='delete-movie'),
]
