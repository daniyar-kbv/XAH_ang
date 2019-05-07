from django.contrib import admin
from django.urls import path
from .views.articleLikeViews import articleLike_list
from .views.commentLikeView import commentLike_list
from .views.auth import Register
from .view.aricleView import ArticleDetailUpdateDelete, ArticleListCreate
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('articles/', ArticleListCreate.as_view()),
    path('articles/<int:pk/', ArticleDetailUpdateDelete.as_view()),
    # path('articles/<int:pk>/likes/', articleLike_list()),
    # path('articles/<int:pk>/likes/<int:pk>/', articleLike_delete.as_view()),
    path('articles/<int:pk>/likes/', articleLike_list.as_view()),
    path('comments/<int:pk>/likes/', commentLike_list),
    path('register/', Register.as_view()),
    path('login/', obtain_jwt_token),
]
