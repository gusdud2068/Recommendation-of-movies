from rest_framework import serializers
from .models import Genre, Top_Movie, Now_Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Top_Movie
        fields="__all__"

class LatestMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Now_Movie
        fields="__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields="__all__"

