from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/likes/',views.movie_likes),
    path('<int:movie_pk>/comments/',views.comment_list),
    path('get_country/', views.save_country_data),
    path('get_genre/', views.save_genre_data),
    path('area/', views.area_list),
    path('area/<int:area_id>/', views.country_by_area),
    path('save_movie/<int:country_id>/', views.save_movie_by_country),
    path('country/', views.country_list),
    path('country/<int:country_id>/', views.movie_by_country),
    path('detail/<int:movie_id>/', views.movie_detail),
]
