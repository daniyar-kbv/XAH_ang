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

    # def get_queryset(self):
    #     return Article.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class ArticleDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Article.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()