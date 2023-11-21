from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comment, Country, Area, Movie, Genre
import requests
from django.conf import settings
from django.http import JsonResponse
from .serializers import CountrySerializer, GenreSerializer, AreaSerializer, MovieSerializer, CommentSerializer

@api_view(['POST'])
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


@api_view(['POST',])
def comment_create(request,movie_pk):
    article = get_object_or_404(Movie,pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET',])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)

@api_view(['DELETE','PUT'])
def comment_detail(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if  request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
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
def save_movie_by_country(request, country_id):

    # 빼야 할 장르 번호 : 12 모험 16 애니메이션 14 판타지 27 공포9648 미스터리 878 SF 53 스릴러
   
    country = get_object_or_404(Country, pk=country_id)
    print(country.iso_3166_1)
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

        serializer = MovieSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
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