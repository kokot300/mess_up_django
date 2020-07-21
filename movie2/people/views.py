from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView

from .forms import PersonForm, RawPersonForm
from .models import Person


# Create your views here.
class PersonListView(ListView):
    queryset = Person.objects.all()
    template_name = 'person/all_person_class.html'


class PersonDetailView(DetailView):
    queryset = Person.objects.all()
    template_name = 'person/all_person_class.html'


def person_details(request, person_id):
    person = Person.objects.get(id=person_id)

    ctxt = {
        'person': person,
    }
    return render(request, 'person/person_details.html', ctxt)


def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    ctxt = {
        'person': person,
    }
    if request.method == 'POST':
        person.delete()
        return redirect('/people/')
    return render(request, 'person/delete_person.html', ctxt)


def all_persons(request):
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        Person.objects.create(first_name=first_name, last_name=last_name)

    order = request.GET.get('order')
    if order == 'ascending':
        people = Person.objects.all().order_by('last_name')
    elif order == 'descending':
        people = Person.objects.all().order_by('-last_name')
    else:
        people = Person.objects.all().order_by('first_name')
    ctxt = {
        'persons': people,
    }
    return render(request, 'person/all_persons.html', ctxt)


def add_raw_person(request):
    form = RawPersonForm()
    if request.method == 'POST':
        form = RawPersonForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Person.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    ctxt = {
        'form': form,
    }
    return render(request, 'person/add_raw_person.html', ctxt)


def add_person(request):
    form = PersonForm(request.POST or None)
    ctxt = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        form = PersonForm()
        return redirect('/people/')

    return render(request, 'person/add_person.html', ctxt)


def edit_person(request, person_id):
    person = Person.objects.get(id=person_id)
    form = PersonForm(request.POST or None, instance=person)
    ctxt = {
        'form': form,
        'person': person,
    }
    if form.is_valid():
        form.save()
        form = PersonForm()
        return redirect('/people/')
    return render(request, 'person/edit_person.html', ctxt)
