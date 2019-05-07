from django.contrib import admin
from .models.articleLikeModel import ArticleLike
from api.models import Article, Comment

# Register your models here.
admin.register(ArticleLike)
admin.site.register(Article)
admin.site.register(Comment)
