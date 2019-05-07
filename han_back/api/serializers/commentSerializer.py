from rest_framework import serializers
from .userSerializer import UserModelSerializer
from .articleSerializer import ArticleSerializer


class CommentSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=255)
    date_published = serializers.DateTimeField()
    created_by = UserModelSerializer(read_only=True)
    article = ArticleSerializer
