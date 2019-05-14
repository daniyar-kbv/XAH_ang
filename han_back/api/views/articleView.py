from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Article
from ..models.category import Category
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
    lookup_field = 'category_id'


    def perform_create(self, serializer):
        try:
            category = Category.objects.get(id=self.kwargs[self.lookup_field])
        except Category.DoesNotExist:
            Response(status.HTTP_404_NOT_FOUND)
        return serializer.save(created_by=self.request.user, category=category)

class ArticleUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Article.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        if self.request.user == self.get_object().created_by:
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ArticleDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Article.objects.get(id=self.kwargs[self.lookup_field])
        
    def perform_destroy(self, instance):
        if self.request.user == self.get_object().created_by:
            instance.delete()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        