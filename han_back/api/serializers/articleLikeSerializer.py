from rest_framework import serializers
from ..models.articleLikeModel import ArticleLike

class ArticleLikeModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = ArticleLike
        fields = ('id','article', 'user')

