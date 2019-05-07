from rest_framework import serializers
from api.models import Category


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = '__all__'
