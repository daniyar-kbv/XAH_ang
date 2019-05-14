from django.contrib import admin
from django.urls import path
from .views.articleLikeViews import articleLike_list
from .views.commentLikeView import commentLike_list
from .views.auth import login, logout, register
from .views.articleView import ArticleDetail, ArticleList, ArticleCreate, ArticleUpdate, ArticleDelete
from rest_framework_jwt.views import obtain_jwt_token
from .views.commentView import CommentList, CommentCreate, CommentDelete
from .views.welcomeView import welcome


urlpatterns = [
    # Welcome page
    path('', welcome),
    # Articles
    path('articles/', ArticleList.as_view()),
    path('articles/create/', ArticleCreate.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
    path('articles/<int:pk>/update/', ArticleUpdate.as_view()),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view()),
    #path('articles/<int:pk>/likes/', articleLike_list()),
    #path('articles/<int:pk>/likes/<int:pk>/', articleLike_delete.as_view()),
    path('articles/<int:pk>/likes/', articleLike_list.as_view()),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),

    # Comments
    path('articles/<int:article_id>/comments/', CommentList.as_view()),
    path('articles/<int:article_id>/comments/create/', CommentCreate.as_view()),
    path('articles/<int:article_id>/comments/<int:pk>/likes/', commentLike_list.as_view()),
    path('comments/delete/<int:pk>/', CommentDelete.as_view())
]
