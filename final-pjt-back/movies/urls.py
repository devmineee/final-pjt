from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('get_country/', views.save_country_data),
    path('get_genre/', views.save_genre_data),
]
