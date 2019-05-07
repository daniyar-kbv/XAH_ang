from rest_framework import serializers
from ..models.articleLikeModel import ArticleLike
from .userSerializer import UserModelSerializer
from .articleSerializer import ArticleSerializer


class ArticleLikeModelSerializer(serializers.ModelSerializer):
    article = ArticleSerializer
    user = UserModelSerializer



    class Meta:
        model = ArticleLike
        fields = ('id','article', 'user')

