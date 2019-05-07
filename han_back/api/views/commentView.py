from rest_framework import generics
from ..models.comment import Comment as Comment
from ..serializers.commentSerializer import CommentSerializer
from ..models.article import Article
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'article_id'

    def get_queryset(self):
        return Comment.objects.comments_article(self.kwargs[self.lookup_field])


class CommentCreate(generics.CreateAPIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = CommentSerializer
    lookup_field = 'article_id'

    def perform_create(self, serializer):
        try:
            article = Article.objects.get(id=self.kwargs[self.lookup_field])
        except Article.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        return serializer.save(created_by=self.request.user, article=article)


class CommentDelete(generics.DestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'pk'

    def get_object(self):
        return Comment.objects.get(id=self.kwargs[self.lookup_field])

    def perform_destroy(self, instance):
        instance.delete()