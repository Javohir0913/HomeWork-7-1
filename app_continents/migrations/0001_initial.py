# Generated by Django 5.0.3 on 2024-03-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent_name', models.CharField(max_length=100, unique=True, verbose_name='Continent Name')),
                ('continent_description', models.TextField(verbose_name='Continent Description')),
                ('continent_image', models.ImageField(upload_to='static/continent/', verbose_name='Continent Image')),
                ('continent_annotations', models.TextField(max_length=150, verbose_name='Continent Annotations')),
                ('continent_date_created', models.DateTimeField(auto_now_add=True, verbose_name='Continent Date')),
            ],
            options={
                'verbose_name': 'Continent',
                'verbose_name_plural': 'Continents',
                'db_table': 'continent',
                'ordering': ['id'],
            },
        ),
    ]