from rest_framework import serializers
from .models import Movie,Comment

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
        
    
class MovieSerializer(serializers.ModelSerializer):
    # 여기선 안했지만 CommentSerializer맘에 안들면 여기서 다시 class작성 가능
    comment_set = CommentSerializer(many=True,read_only= True) # 1:N관계이므로 many = True # 직접 입력받는 것도 아니고 활성화 시켰기 때문에 read_only해야
    # 신규 필드 작성(serializer에 작성)
    # 여긴 article모델을 기반으로 한것이기에 article.comment_set.count()에서 변형 된 것
    comment_count = serializers.IntegerField(source='comment_set.count',read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'