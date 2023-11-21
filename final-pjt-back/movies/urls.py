from django.urls import path
from . import views
urlpatterns = [

    path('get_country/', views.save_country_data),
    path('get_genre/', views.save_genre_data),
    path('area/', views.area_list),
    path('area/<int:area_id>/', views.country_by_area),
    path('save_movie/<int:country_id>/', views.save_movie_by_country),
]
