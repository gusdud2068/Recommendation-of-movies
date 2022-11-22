from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
path('',views.index,name='index'),
    path('now/', views.now, name='now'),
    # 댓글 목록
    path('comments/', views.comment_list),
    # path('comments/<int:movie_pk>/', views.movie_comments),
    # 최신영화에 댓글 조회, 수정, 삭제
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 최신영화에 댓글 생성
    path('movie/<int:movie_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/like/', views.like),
   
]
