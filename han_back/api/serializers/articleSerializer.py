from django.contrib.auth.models import User
from rest_framework import serializers
<<<<<<< HEAD
# from .article import Article
# from .serializers import UserModelSerializer
from api.serializers import CategorySerializer, UserModelSerializer
=======
from ..models import Article
from ..serializers import UserModelSerializer
from ..serializers.categorySerializer import CategorySerializer
>>>>>>> 3b244a764b43f2142820e9517fb16c4df10e5624
from api.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    views = serializers.IntegerField(required=False)
    imageUrl = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    created_by = UserModelSerializer
    category = CategorySerializer

    def create(self, validated_data):
        article = Article(**validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance