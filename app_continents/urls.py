from django.urls import path

from .views import (
    index,
    continent_show,
    edit_continent,
    delete_continent,
    create_continent,
    about,
    create_country,
    edit_country,
    delete_country
)


urlpatterns = [
    path('', index, name='index'),
    path('create/', create_continent, name='create_continent'),
    path('about/', about, name='about'),
    path('<int:pk>/', continent_show, name='continent_show'),
    path('edit/<int:pk>/', edit_continent, name='edit_continent'),
    path('delete/<int:pk>/', delete_continent, name='delete_continent'),
    path('country/', create_country, name='create_country'),
    path('edit_county/<int:pk>/', edit_country, name='edit_country'),
    path('delete_county/<int:pk>/', delete_country, name='delete_country'),
]