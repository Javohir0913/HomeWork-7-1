from django.forms import ModelForm

from .models import Continent, Country


class ContinentForm(ModelForm):
    class Meta:
        model = Continent
        fields = ['continent_name', 'continent_annotations', 'continent_description', 'continent_image']


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['country_name', 'country_continent']