from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comment, Country, Area, Movie, Genre
import requests
from django.conf import settings
from django.http import JsonResponse
from .serializers import CountrySerializer, GenreSerializer, AreaSerializer, MovieSerializer, CommentSerializer, MovieSaveSerializer

@api_view(['POST','GET'])
def movie_likes(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method == 'POST':
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
            is_liked = False
        else:
            movie.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
            'likes_count' : movie.like_users.count()
        }
        return JsonResponse(context)
    elif request.method == 'GET':
        if request.user in movie.like_users.all():
            is_liked = True
        else:
            is_liked = False
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
        

@api_view(['POST','GET',])
def comment_list(request,movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = movie.comment_set.all()
        # comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)


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

        # 아시아
        if save_data["iso_3166_1"] in ["IN","JP","TH","HK"]:
            save_data["area"] = 1

        # 서유럽
        elif save_data["iso_3166_1"] in ["GB","FR","DE","ES","IT","NL"]:
            save_data["area"] = 2

        # 동유럽/중동
        elif save_data["iso_3166_1"] in ["RU","TR","SA","GR"]:
            save_data["area"] = 3

        # 남/북미
        elif save_data["iso_3166_1"] in ["US","MX", "BR", "AR"]:
            save_data["area"] = 4

        serializer = CountrySerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


    return Response(response)


@api_view(['GET',])
def save_genre_data(request):

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
def save_movie_by_country(request, country_id, page):

    # 빼야 할 장르 번호 : 12 모험 16 애니메이션 14 판타지 27 공포9648 미스터리 878 SF 53 스릴러
   
    country = get_object_or_404(Country, pk=country_id)
    print(country.iso_3166_1)
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko&page={page}&sort_by=popularity.desc&vote_count.gte=200&with_origin_country={country.iso_3166_1}&without_genres=36%2C%2012%2C%2016%2C%2014%2C%2027%2C%209648%2C%20878%2C%2053"
    response = requests.get(url, headers=headers).json()

    for movie in response.get('results'):

        if Movie.objects.filter(pk=movie.get('id')).exists():
            movie = Movie.objects.get(pk=movie.get('id'))
            movie.countries.add(country.id)
            continue
        
        save_data = {
            'title' : movie.get('title'),
            'release_date' : movie.get('release_date'),
            'popularity' : movie.get('popularity'),
            'vote_count' : movie.get('vote_count'),
            'vote_average' : movie.get('vote_average'),
            'overview' : movie.get('overview'),
            'poster_path' : movie.get('poster_path'),
        }

        if not save_data['overview']:
            save_data['overview'] = "등록된 줄거리가 없습니다."

        serializer = MovieSaveSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(id=movie.get('id'))
        genres = movie.get('genre_ids')
        movie = Movie.objects.get(pk=movie.get('id'))
        for genre in genres:
            movie.genres.add(genre)
        movie.countries.add(country.id)

    return Response(response)
            


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

@api_view(['GET',])
def country_list(request):
    countries = get_list_or_404(Country)
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def movie_by_country(request, country_id):
    movies = get_list_or_404(Movie, countries=country_id)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)