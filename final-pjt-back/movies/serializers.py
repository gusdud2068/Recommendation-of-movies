from rest_framework import serializers
from .models import Genre, Top_Movie, Now_Movie, Comments


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=("name",)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Top_Movie
        fields="__all__"

class LatestMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Now_Movie
        fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'like_users', )


