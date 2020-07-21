from django import forms
from .models import Movie, RoleMovie, Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'name'
        ]


class MovieForm(forms.ModelForm):
    # title = forms.CharField()
    # director = forms.CharField()
    # screenplay = forms.CharField()
    # starring = forms.CharField()
    # year = forms.IntegerField()
    # rating = forms.FloatField(max_value=5)
    # genre = forms.CharField()
    # role = forms.CharField(max_length=60, initial)

    class Meta:
        model = Movie
        fields = '__all__'
        #     [
        #     'title',
        #     'director',
        #     'screenplay',
        #     'starring',
        #     'role',
        #     'year',
        #     'rating',
        #     'genre',
        #
        # ]
