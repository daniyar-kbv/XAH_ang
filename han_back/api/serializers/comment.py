from rest_framework import serializers
from ..models.comment import Comment
from .user import UserModelSerializer


class CommentSerializer(serializers.Serializer):
    created_by = UserModelSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
