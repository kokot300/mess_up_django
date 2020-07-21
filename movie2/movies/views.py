from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MovieForm
from .models import Genre, Movie, RoleMovie


# Create your views here.


def movie_details(request, movie_id):
    # movie = Movie.objects.get(id=movie_id)
    movie = get_object_or_404(Movie, id=movie_id)
    starring = RoleMovie.objects.all().filter(movie=movie)
    print(movie.title)
    ctxt = {
        'movie': movie,
        'starring': starring,
    }
    return render(request, 'movie/movie_details.html', ctxt)


def all_movies(request):
    order = request.GET.get('order')
    if order == 'ascending':
        movies = Movie.objects.all().order_by('rating')
    elif order == 'descending':
        movies = Movie.objects.all().order_by('-rating')
    else:
        movies = Movie.objects.all()
    ctxt = {
        'movies': movies,
    }
    return render(request, 'movie/all_movies.html', ctxt)


def add_movie(request):
    # MovieFromSet = inlineformset_factory(Movie, RoleMovie, fields=('person', 'role'))
    # formset = MovieFromSet

    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MovieForm(request.POST or None)
    ctxt = {
        'formset': form,
        'movie': Movie,
    }
    return render(request, 'movie/add_movie.html', ctxt)


def edit_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, instance=movie)
    ctxt = {
        'form': form,
        'movie': movie,
    }
    if form.is_valid():
        form.save()
        form = MovieForm()
        return redirect('/movies/')
    return render(request, 'movie/edit_movie.html', ctxt)


def add_genre(request):
    new_genre = request.POST.get('genre')
    if request.method == 'POST':
        Genre.objects.create(name=new_genre)
    ctxt = {
        'genre': Genre
    }
    return render(request, 'genre/add_genre.html', ctxt)


def search_movie(request):
    directions = {
        'search_by_title': 1,
        'search_by_first_name': 1,
        'search_by_last_name': 1,
        'search_by_year': 1,
        'search_by_rating': 1,
        'search_by_genre': 1,
    }
    ctxt = {}

    title = request.GET.get('title')
    if title is None:
        title = ''
    first_name = request.GET.get('first_name')
    if first_name is None:
        first_name = ''
    last_name = request.GET.get('last_name')
    if last_name is None:
        last_name = ''
    try:
        year_from = int(request.GET.get('year_from'))
        year_to = int(request.GET.get('year_to'))

        rating_from = float(request.GET.get('rating_from'))
        rating_to = float(request.GET.get('rating_to'))
    except TypeError:
        pass

    genre = request.GET.get('genre')
    if genre is None:
        genre = ''

    search_by_title = request.GET.get('search_by_title')
    search_by_first_name = request.GET.get('search_by_first_name')
    search_by_last_name = request.GET.get('search_by_last_name')
    search_by_year = request.GET.get('search_by_year')
    search_by_rating = request.GET.get('search_by_rating')
    search_by_genre = request.GET.get('search_by_genre')

    movies = Movie.objects.all()
    if search_by_title == '1':
        movies = movies.filter(title__icontains=title)
    elif search_by_first_name == '1':
        movies = movies.filter(director__first_name__icontains=first_name)
    elif search_by_last_name == '1':
        movies = movies.filter(director__last_name__icontains=last_name)
    elif search_by_year == '1':
        movies = movies.filter(year__gte=year_from, year__lte=year_to)
    elif search_by_rating == '1':
        movies = movies.filter(rating__gte=rating_from, rating__lte=rating_to)
    elif search_by_genre == '1':
        movies = movies.filter(genre__name__icontains=genre)
    else:
        return render(request, 'movie/search_movie.html', ctxt)

    # movies = Movie.objects.all().filter(title__icontains=title)
    # movies = movies.filter(director__icontains=first_name)

    ctxt = {
        'movies': movies
    }
    return render(request, 'movie/search_movie.html', ctxt)


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    ctxt = {
        'movie': movie,
    }
    if request.method == 'POST':
        movie.delete()
        return redirect('/movies/')
    return render(request, 'movie/delete_movie.html', ctxt)
