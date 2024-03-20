from django.db import models


# Create your models here.
class Continent(models.Model):
    continent_name = models.CharField(max_length=100, verbose_name='Continent Name', unique=True)
    continent_description = models.TextField(verbose_name='Continent Description')
    continent_image = models.ImageField(upload_to='continent/', verbose_name='Continent Image')
    continent_annotations = models.TextField(max_length=150, verbose_name='Continent Annotations')
    continent_date_created = models.DateTimeField(auto_now_add=True, verbose_name='Continent Date')

    def __str__(self):
        return self.continent_name

    class Meta:
        verbose_name = 'Continent'
        verbose_name_plural = 'Continents'
        db_table = 'continent'
        ordering = ['id']


class Country(models.Model):
    country_name = models.CharField(max_length=100, verbose_name='Country Name', unique=True)
    country_continent = models.ForeignKey(Continent, verbose_name='Continent Id', on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'country'
