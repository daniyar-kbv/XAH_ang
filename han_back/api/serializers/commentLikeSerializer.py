from rest_framework import serializers
from ..models.commentLikeModel import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CommentLike
        fields = '__all__'
