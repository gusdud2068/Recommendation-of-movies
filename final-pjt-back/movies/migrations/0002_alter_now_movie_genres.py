# Generated by Django 3.2.9 on 2022-11-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now_movie',
            name='genres',
            field=models.ManyToManyField(related_name='now_movie_genre', to='movies.Genre'),
        ),
    ]
