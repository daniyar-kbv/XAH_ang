from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Article

class ContactSerializer(serializers.ModelSerializer):

    # created_by = UserSerializer
    # category = CategorySerializer

    class Meta:
        model = Article
        fields = '__all__'