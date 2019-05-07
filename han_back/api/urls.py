from django.contrib import admin
from django.urls import path
from api.views import articleView, articleLikeViews


urlpatterns = [
    path('articles/', articleView.ArticleListCreate.as_view()),
    path('articles/<int:pk/', articleView.ArticleDetailUpdateDelete.as_view()),
    path('articles/<int:pk>/likes', articleLikeViews.articleLike_list.as_view()),
    path('articles/<int:pk>/likes/<int:pk>/', articleLikeViews.articleLike_delete()),
]
