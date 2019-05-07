from ..models.articleLikeModel import ArticleLike
from django.http import JsonResponse
from ..serializers.articleLikeSerializer import ArticleLikeModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

class articleLike_list(APIView):
	def get(self, request):
		likes = ArticleLike.objects.all()
		serializer = ArticleLikeModelSerializer(likes, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ArticleLikeModelSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	def delete(self, request, pk):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


