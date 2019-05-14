from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Article
from api.serializers import ArticleSerializer

class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('views', 'created_at')
    filterset_fields = ('category',)

class ArticleDetail(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        article = Article.objects.get(id=self.kwargs[self.lookup_field])
        article.views += 1
        article.save()
        return article

class ArticleCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

class ArticleUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Article.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        serializer.save()

class ArticleDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Article.objects.get(id=self.kwargs[self.lookup_field])
    def perform_destroy(self, instance):
        instance.delete()