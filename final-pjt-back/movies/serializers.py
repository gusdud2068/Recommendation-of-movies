from rest_framework import serializers
from .models import Genre, Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields="__all__"

