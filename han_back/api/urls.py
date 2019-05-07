from django.contrib import admin
from django.urls import path
from .views.articleLikeViews import articleLike_list
from .views.auth import Register
from rest_framework_jwt.views import obtain_jwt_token
from .views.commentView import CommentList, CommentCreate


urlpatterns = [
    path('articles/<int:pk>/likes/', articleLike_list.as_view()),
    path('register/', Register.as_view()),
    path('login/', obtain_jwt_token),

    # Comments
    path('articles/<int:article_id>/comments/', CommentList.as_view()),
    path('articles/<int:article_id>/comments/create/', CommentCreate.as_view())
]