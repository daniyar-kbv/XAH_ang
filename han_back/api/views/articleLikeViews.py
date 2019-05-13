from ..models.articleLikeModel import ArticleLike
from django.http import JsonResponse
from ..serializers.articleLikeSerializer import ArticleLikeModelSerializer
from rest_framework import status, request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ..models.article import Article
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class articleLike_list(APIView):
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, pk):
        likes = ArticleLike.objects.all()
        serializer = ArticleLikeModelSerializer(likes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ArticleLikeModelSerializer(data=request.data)

        try:
            article = Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)


        articlelikes = ArticleLike.objects.filter(user=request.user, article=Article.objects.get(id=pk))

        if (serializer.is_valid() and len(articlelikes)==0):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_302_FOUND)

        return Response(status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        like = self.get_object(pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

