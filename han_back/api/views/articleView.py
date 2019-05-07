from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.models import Article
from api.serializers import ArticleSerializer


class ArticleListCreate(generics.ListCreateAPIView):

    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class ArticleDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        article = Article.objects.get(id=self.kwargs[self.lookup_field])
        article.views += 1
        article.save()
        return article

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# class ArticleDetail(generics.RetrieveAPIView):
#     serializer_class = ArticleSerializer
#     lookup_field = 'pk'

#     def get_object(self):
#         article = Article.objects.get(id=self.kwargs[self.lookup_field])
#         article.views += 1
#         return article


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        article = Article.objects.get(id=self.kwargs[self.lookup_field])
        article.views += 1
        article.save()
        return article

