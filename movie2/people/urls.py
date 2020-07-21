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

from .views import (add_person,
                    add_raw_person,
                    all_persons,
                    person_details,
                    edit_person,
                    delete_person,
                    PersonListView)

urlpatterns = [
    path('add/', add_person, name='add-person'),
    path('add_raw/', add_raw_person, name='add_raw_person'),
    path('', all_persons, name='persons'),
    path('class/', PersonListView.as_view(), name='persons-class'),
    path('<int:person_id>/details/', person_details, name='person-details'),
    path('<int:person_id>/edit/', edit_person, name='edit-person'),
    path('<int:person_id>/delete/', delete_person, name='delete-person'),
]