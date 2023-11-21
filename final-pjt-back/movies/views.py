from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
import requests
import django
from django.conf import settings
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Country, Area, Movie, Genre
from .serializers import CountrySerializer, GenreSerializer, AreaSerializer, MovieSerializer


TMDB_ACCESS_TOKEN = settings.TMDB_ACCESS_TOKEN

headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}"}

@api_view(['GET',])
def save_country_data(request):

    url = "https://api.themoviedb.org/3/configuration/countries?language=ko"

    response = requests.get(url, headers=headers).json()

    for country in response:
        save_data = {
            'iso_3166_1' : country.get('iso_3166_1'),
            'english_name' : country.get('english_name'),
            'korean_name':country.get('native_name'),
        }

        # 동아시아
        if save_data["iso_3166_1"] in ["KR","CN","JP","TW","HK"]:
            save_data["area"] = 1

        # 동남아시아
        elif save_data["iso_3166_1"] in ["TH", "VN", "SG", "PH", "ID"]:
            save_data["area"] = 2

        # 중앙아시아
        elif save_data["iso_3166_1"] in ["MN","KZ","UZ"]:
            save_data["area"] = 3

        # 남아시아
        elif save_data["iso_3166_1"] in ["IN","PK"]:
            save_data["area"] = 4

        # 중동
        elif save_data["iso_3166_1"] in ["IL","EG","TR","IR","SA"]:
            save_data["area"] = 5

        # 북미
        elif save_data["iso_3166_1"] in ["US", "CA"]:
            save_data["area"] = 6

        # 남미
        elif save_data["iso_3166_1"] in ["MX","BR","AR","CL","CO"]:
            save_data["area"] = 7

        # 유럽
        elif save_data["iso_3166_1"] in ["GB","FR","DE","ES","IT","CZ","SE"]:
            save_data["area"] = 8

        # 오세아니아
        elif save_data["iso_3166_1"] in ["NZ","AU"]:
            save_data["area"] = 9

        # 아프리카
        elif save_data["iso_3166_1"] in ["NG","ET","CD","ZA","TZ"]:
            save_data["area"] = 10

        serializer = CountrySerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    return Response(response)


@api_view(['GET',])
def save_genre_data(request):

    Genre.objects.all().delete()
    
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

    response = requests.get(url, headers=headers).json()

    for genre in response.get('genres'):
        print(genre)
        save_data = {
            'name' : genre.get('name')
        }
        serializer = GenreSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(id=genre.get('id'))

    return Response(response)


@api_view(['GET',])
def save_movie_by_country(request):

    # 빼야 할 장르 번호 : 12 모험 16 애니메이션 14 판타지 27 공포9648 미스터리 878 SF 53 스릴러
   
    countries = get_list_or_404(Country)

    for country in countries:
        page = 1
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko&page={page}&sort_by=popularity.desc&vote_count.gte=200&with_origin_country={country.iso_3166_1}&without_genres=36%2C%2012%2C%2016%2C%2014%2C%2027%2C%209648%2C%20878%2C%2053"
        response = requests.get(url, headers=headers).json()

        for movie in response.get('results'):
            save_data = {
                'title' : movie.get('title'),
                'release_date' : movie.get('release_date'),
                'popularity' : movie.get('popularity'),
                'vote_count' : movie.get('vote_count'),
                'vote_average' : movie.get('vote_average'),
                'overview' : movie.get('overview'),
                'poster_path' : movie.get('poster_path'),
            }

            movie = Movie.objects
            serializer = MovieSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            


@api_view(['GET',])
def area_list(request):
    areas = get_list_or_404(Area)
    serializer = AreaSerializer(areas, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def country_by_area(request, area_id):
    countries = get_list_or_404(Country, area_id=area_id)
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)