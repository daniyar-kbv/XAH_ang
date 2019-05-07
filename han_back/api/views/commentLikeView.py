from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from ..models.comment import Comment
from ..models.commentLikeModel import CommentLike
from ..serializers.categorySerializer import CategorySerializer
from ..serializers.commentLikeSerializer import CommentLikeSerializer
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def commentLike_list(request, pk):
	if request.method == 'GET':
		likes = CommentLike.objects.get(id=pk)
		serializer = CommentLikeSerializer(likes, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = CommentLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class commentLike_delete(APIView):
	def delete(self, request, pk):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
