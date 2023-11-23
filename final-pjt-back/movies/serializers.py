from rest_framework import serializers
from .models import Movie, Genre, Area, Country, Comment


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    countries = CountrySerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('countries', 'genres', 'like_users',)


class CommentSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    # overide
    movie = MovieSerializer(read_only= True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('movie',) #위에서 override해서!