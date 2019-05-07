from django.contrib import admin
from django.urls import path
from han_back.api.views.articleLikeViews import articleLike_list, articleLike_delete


urlpatterns = [
    path('articles/<int:pk>/likes', articleLike_list.as_view()),
    path('articles/<int:pk>/likes/<int:pk>/', articleLike_delete()),
]
