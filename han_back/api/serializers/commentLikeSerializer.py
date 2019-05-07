from rest_framework import serializers
from ..models.commentLikeModel import CommentLike
from .userSerializer import UserModelSerializer
from .commentSerializer import CommentSerializer


class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    owner = UserModelSerializer

    class Meta:
        model = CommentLike
        fields = '__all__'
