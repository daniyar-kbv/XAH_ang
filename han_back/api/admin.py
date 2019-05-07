from django.contrib import admin
from .models.articleLikeModel import ArticleLike
from .models.article import Article
from .models.comment import Comment

# Register your models here.
admin.register(ArticleLike)
admin.site.register(Article)
admin.site.register(Comment)