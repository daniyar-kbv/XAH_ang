from django.contrib import admin
from .models.articleLikeModel import ArticleLike
from .models.article import Article
from .models.comment import Comment
from .models.category import Category
from .adminModels.commentAdmin import CommentAdmin
from .models.commentLikeModel import CommentLike

# Register your models here.
admin.site.register(ArticleLike)
admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(CommentLike)