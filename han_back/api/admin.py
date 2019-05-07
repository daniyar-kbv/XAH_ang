from django.contrib import admin
from .models.articleLikeModel import ArticleLike
from .models.article import Article
from .models.comment import Comment
from .models.category import Category

# Register your models here.
admin.site.register(ArticleLike)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)