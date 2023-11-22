from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('<int:user_pk>/profile/',views.custom_getUserInfo, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/like_movies/',views.getLikeMovies)
]