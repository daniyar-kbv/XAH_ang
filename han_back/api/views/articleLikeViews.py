from ..models.articleLikeModel import ArticleLike
from django.http import JsonResponse
from ..serializers.articleLikeSerializer import ArticleLikeModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ..models import Article
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class articleLike_list(APIView):
	authentication_classes = (JSONWebTokenAuthentication, )

	def get(self, request, pk):
		task_lists = ArticleLike.objects.all()
		serializer = ArticleLikeModelSerializer(task_lists, many=True)
		return Response(serializer.data)

	def post(self, request, pk):
		serializer = ArticleLikeModelSerializer(data=request.data)

		try:
			article = Article.objects.get(id=pk)
		except Article.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)

		if serializer.is_valid():
			serializer.save(user=request.user, article=article)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	def delete(self, request, pk):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


