from rest_framework import serializers
from .userSerializer import UserModelSerializer
from .articleSerializer import ArticleSerializer
from ..models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    body = serializers.CharField(max_length=255)
    date_published = serializers.DateTimeField(read_only=True)
    created_by = UserModelSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)