from rest_framework import serializers
from api.models import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CommentLike
        fields = '__all__'
