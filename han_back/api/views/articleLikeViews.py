from ..models.articleLikeModel import ArticleLike
from django.http import JsonResponse
from ..serializers.articleLikeSerializer import ArticleLikeModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def articleLike_list(request, pk):
	if request.method == 'GET':
		likes = ArticleLike.objects.get(id=pk)
		serializer = ArticleLikeModelSerializer(likes, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ArticleLikeModelSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

class articleLike_delete(APIView):
	def delete(self, request, pk):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)