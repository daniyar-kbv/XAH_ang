from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    imageUrl = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)

    # created_by = UserSerializer
    # category = CategorySerializer