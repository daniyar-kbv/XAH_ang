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
from ..serializers.articleSerializer import ArticleModelSerializer

class IsStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class ArticleList(generics.ListAPIView):
    authentication_classes = ()
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('views', 'created_at')
    filterset_fields = ('category',)

class ArticleListByUser(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(created_by=self.request.user)

class ArticleDetail(generics.RetrieveAPIView):
    authentication_classes = ()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    def get_object(self):
        article = Article.objects.get(id=self.kwargs[self.lookup_field])
        article.views += 1
        article.save()
        return article

class ArticleCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsStaff, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleModelSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

class ArticleUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsStaff, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ArticleModelSerializer
    lookup_field = 'pk'

    def get_object(self):
        return Article.objects.get(id=self.kwargs[self.lookup_field])

    def perform_update(self, serializer):
        if self.request.user == self.get_object().created_by:
            serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ArticleDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, IsStaff, )
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
        