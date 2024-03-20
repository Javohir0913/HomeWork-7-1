from django.shortcuts import render, get_object_or_404, redirect

from .models import Continent, Country
from .forms import ContinentForm


# Create your views here.
def index(request):
    continents = Continent.objects.all()
    return render(request, 'continents/index.html', context={'continents': continents})


def about(request):
    continents = Continent.objects.all()
    return render(request, 'continents/about.html', context={'continents': continents})


def continent_show(request, pk):
    # Continent.objects.filter(pk=pk).update(name=F('image')+1)
    continent = Continent.objects.get(pk=pk)
    continents = Continent.objects.all()
    countries = Country.objects.all()
    return render(request, 'continents/continent_info.html',
                  context={'continent': continent, 'continents': continents, 'countries': countries})


def create_continent(request):
    if request.method == 'POST':
        form = ContinentForm(request.POST, request.FILES)
        continent = form.save()
        return redirect('index')

    else:
        form = ContinentForm()
        all_continents = Continent.objects.all()
        return render(request, 'continents/create_continent.html',
                      context={'continents': all_continents, 'form': form})


def edit_continent(request, pk):
    continent = get_object_or_404(Continent, id=pk)
    if request.method == 'POST':
        form = ContinentForm(request.POST, request.FILES, instance=continent)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ContinentForm(instance=continent)
        all_continents = Continent.objects.all()
        return render(request, 'continents/edit_continent.html',
                      context={'continents': all_continents, 'form': form})


from django.contrib import messages


def delete_continent(request, pk):
    continent = get_object_or_404(Continent, id=pk)

    if request.method == 'POST':
        continent.delete()
        messages.success(request, 'Continent deleted successfully.')
        return redirect('index')
    else:
        all_continents = Continent.objects.all()
        return render(request, 'continents/delete_continent.html',
                      context={'continent': continent, 'continents': all_continents})


def create_country(request):
    all_continents = Continent.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        continent = request.POST['continent']
        number = Continent.objects.get(continent_name=continent)
        new_country = Country(country_name=name, country_continent_id=number.id)
        new_country.save()
        return redirect('continent_show', pk=new_country.country_continent_id)
    else:
        return render(request, 'country/create_country.html', context={'all_continents': all_continents})


def edit_country(request, pk):
    this_country = get_object_or_404(Country, pk=pk)
    all_continents = Continent.objects.all()
    if request.method == 'POST':
        this_country.country_name = request.POST['country_name']
        continent = request.POST['continent_id']
        print(continent)
        new_continent = Continent.objects.get(continent_name=continent)
        number = Continent.objects.get(continent_name=new_continent)
        this_country.country_continent_id = number.id
        this_country.save()
        return redirect('index')

    else:
        return render(request, 'country/edit_country.html',
                      context={'all_continents': all_continents, 'this_country': this_country})


def delete_country(request, pk):
    this_country = get_object_or_404(Country, pk=pk)
    all_continents = Continent.objects.all()
    if request.method == 'POST':
        this_country.delete()
        return redirect('index')
    else:
        return render(request, 'country/delete_country.html',
                      context={'continent': this_country, 'continents': all_continents})

