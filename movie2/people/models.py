from django.db import models
from django.urls import reverse


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    class Meta:
        ordering = ['last_name']

    @property
    def get_add_url(self):
        return reverse("add-person", kwargs={})

    @property
    def get_absolute_url(self):
        return reverse("persons", kwargs={})

    @property
    def get_detail_url(self):
        return reverse("person-details", kwargs={'person_id': self.id})

    @property
    def get_edit_url(self):
        return reverse("edit-person", kwargs={'person_id': self.id})

    @property
    def get_delete_url(self):
        return reverse("delete-person", kwargs={'person_id': self.id})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
