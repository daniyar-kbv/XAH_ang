from django.contrib.auth.models import User
from rest_framework import serializers
from .article import Article
from api.serializers import UserModelSerializer
from api.serializers import CategorySerializer
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