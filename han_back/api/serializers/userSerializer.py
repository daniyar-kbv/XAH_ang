from rest_framework import serializers
from django.contrib.auth.models import User


class UserModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.get("password")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        return user

    class Meta:
        model = User
        fields = '__all__'
