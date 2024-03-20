from django.forms import ModelForm

from .models import Continent


class ContinentForm(ModelForm):
    class Meta:
        model = Continent
        fields = ['continent_name', 'continent_annotations', 'continent_description', 'continent_image']