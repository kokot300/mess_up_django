#!/usr/bin/python
from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
        ]


class RawPersonForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(label='last_name', initial='Pazura')