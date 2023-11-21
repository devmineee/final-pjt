from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import AccountSerializer, FollowingSerializer
from rest_framework.response import Response
# Create your views here.
# @login_required # 여기서 해줘야되나??
@api_view(["POST"])
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False
        else:
            you.followers.add(me)
            is_followed = True
        context = {
            'is_followed' : is_followed,
            'followings_count': you.followings.count(),
            'followers_count': you.followers.count(),
        }
        return JsonResponse(context)
    # return JsonResponse('내가 나를 follow할 때...') // 막아야 한다.
    
@api_view(['GET'])
def custom_getUserInfo(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    serializer = AccountSerializer(user)
    return Response(serializer.data)
  
def getLikeMovies(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    like_movies = user.movie_set.all()
    context = {
        'like_movies' : like_movies, 
    }
    return JsonResponse(context)
    
