from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.index,name='index'),
    path('now/', views.now, name='now'),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movie/<int:movie_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/like', views.like),
   
]
