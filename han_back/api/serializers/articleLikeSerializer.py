from rest_framework import serializers
from han_back.api.models.articleLikeModel import ArticleLike

class ArticleLikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLike
        fields = ('id','article', 'user')

