from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from ..models.comment import Comment
from ..models.commentLikeModel import CommentLike
from ..serializers.categorySerializer import CategorySerializer
from ..serializers.commentLikeSerializer import CommentLikeSerializer
from rest_framework.views import APIView


class commentLike_list(APIView):
	def get(self, request, pk):
		likes = CommentLike.objects.all()
		serializer = CommentLikeSerializer(likes, many=True)
		return Response(serializer.data)

	def post(self, request, pk):
		serializer = CommentLikeSerializer(data=request.data)
		try:
			comment = Comment.objects.get(id=pk)
		except Comment.DoesNotExist:
			return Response(status.HTTP_404_NOT_FOUND)


		commentlikes = CommentLike.objects.filter(user=request.user, comment=Comment.objects.get(id=pk))
		if (serializer.is_valid() and len(commentlikes)==0):
			serializer.save(user=request.user, comment=comment)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(status.HTTP_302_FOUND)

		return Response(status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
