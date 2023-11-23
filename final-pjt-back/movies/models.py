from django.db import models
from django.conf import settings

# 모든 장르의 종류가 저장되는 테이블
class Genre(models.Model):
    name = models.CharField(max_length=20)


# 지역을 정의하는 필드
class Area(models.Model):
    name = models.CharField(max_length=30)


# 모든 나라의 정보를 담은 테이블
class Country(models.Model):
    english_name = models.CharField(max_length=100)
    korean_name = models.CharField(max_length=100, null=True)
    iso_3166_1 = models.CharField(max_length=2)
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)


# 모든 영화가 저장되는 테이블
class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200)
    # 중개 테이블
    countries = models.ManyToManyField(Country, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # 추가한 것
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)