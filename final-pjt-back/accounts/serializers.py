from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

class FollowingSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('id','username',)


class AccountSerializer(serializers.ModelSerializer):
    followers = FollowingSerializer(many=True,read_only=True)
    followers_count = serializers.IntegerField(source='followers.count',read_only=True)
    followings = FollowingSerializer(many=True,read_only=True)
    followings_count = serializers.IntegerField(source='followings.count',read_only=True)
    class Meta:
      model = get_user_model()
      fields = ('id','username','followers','followings','followers_count','followings_count')