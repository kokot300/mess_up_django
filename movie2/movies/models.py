from django.db import models
from django.urls import reverse

from people.models import Person


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=32)

    @property
    def get_add_url(self):
        return reverse("add-genre", kwargs={})

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='+')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='+')
    starring = models.ManyToManyField(Person, through='RoleMovie')
    year = models.IntegerField(max_length=4)
    rating = models.FloatField(max_length=4)
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['year']

    @property
    def get_detail_url(self):
        return reverse("movie-details", kwargs={'movie_id': self.id})
        # return f"/movie_detail/{self.id}/"

    @property
    def get_edit_url(self):
        return reverse("edit-movie", kwargs={'movie_id': self.id})

    @property
    def get_absolute_url(self):
        return reverse("movie-list", kwargs={})

    @property
    def get_add_url(self):
        return reverse("add-movie", kwargs={})

    @property
    def get_delete_url(self):
        return reverse("delete-movie", kwargs={'movie_id': self.id})

    def __str__(self):
        return f'{self.title}'


class RoleMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)
