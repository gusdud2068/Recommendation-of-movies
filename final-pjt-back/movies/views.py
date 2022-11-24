from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Top_Movie, Genre, Now_Movie, Comments
from .serializers import MovieListSerializer, GenreSerializer, LatestMovieSerializer, CommentSerializer


# Create your views here.
@api_view(["GET"])
def index(request):
    if request.method == "GET":
        # movies = Now_Movie.objects.all().union(Top_Movie.objects.all()).order_by('-id')
        # serializer = MovieListSerializer(movies, many=True)
        movies_now = Now_Movie.objects.all().order_by('-id')
        serializer_now = LatestMovieSerializer(movies_now, many=True)
        movies_top = Top_Movie.objects.all().order_by('-id')
        serializer_top = MovieListSerializer(movies_top, many=True)
        result = serializer_now.data + serializer_top.data
        # print(result) 
        return Response(result, status=status.HTTP_200_OK)

@api_view(["GET"])
def now(request):
    if request.method == "GET":
        movies = Now_Movie.objects.all()
        serializer = LatestMovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comments.objects.all()
        comments = get_list_or_404(Comments)
        # print(comments)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comments.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comments, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Now_Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    user = request.user
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def like(request, comment_pk):
    if request.user.is_authenticated:
        comment= Comments.objects.get(pk=comment_pk)
        user = request.user

        if comment.like_users.filter(pk=user.pk).exists():
            comment.like_users.remove(user)
            is_liked = False
        else:
            comment.like_users.add(user)
            is_liked = True
        return Response ({"is_liked":is_liked,'like_count':comment.like_users.count()})
    return Response({'message': '로그인 후 이용가능합니다.'}, status=status.HTTP_401_UNAUTHORIZED)

