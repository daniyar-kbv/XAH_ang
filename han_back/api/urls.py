from django.contrib import admin
from django.urls import path
from han_back.api.views.articleLikeViews import articleLike_list, articleLike_delete
from han_back.api.views.auth import Register
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('articles/<int:pk>/likes', articleLike_list.as_view()),
    path('articles/<int:pk>/likes/<int:pk>/', articleLike_delete()),
    path('register/', Register.as_view()),
    path('login/', obtain_jwt_token),
]
