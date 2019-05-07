from rest_framework import generics
from ..models.comment import Comment
from ..serializers.commentSerializer import CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'article_id'

    def get_queryset(self):
        return Comment.comments_by_article.get_queryset(self.kwargs[self.lookup_field])

