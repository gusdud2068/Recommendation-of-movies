from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Top_Movie, Genre, Now_Movie
from .serializers import MovieListSerializer, GenreSerializer, LatestMovieSerializer


# Create your views here.
@api_view(["GET"])
def index(request):
    if request.method == "GET":
        movies = Top_Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def now(request):
    if request.method == "GET":
        movies = Now_Movie.objects.all()
        serializer = LatestMovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
