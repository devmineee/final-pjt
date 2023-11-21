from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/likes/',views.movie_likes),
    path('<int:movie_pk>/comments/',views.comment_create),
    path('comments/',views.comment_list),
]
