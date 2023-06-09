# Generated by Django 3.2.9 on 2022-11-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_now_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now_movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
        migrations.AlterField(
            model_name='top_movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
