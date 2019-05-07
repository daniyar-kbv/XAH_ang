from django.db import models
from django.contrib.auth.models import User
from .article import Article
from datetime import datetime


class CommentArticleManager(models.Manager):
    def get_queryset(self, article):
        return super().get_queryset().filter(article=article)


class Comment(models.Model):
    body = models.CharField(max_length=255)
    date_published = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    comments_by_article = CommentArticleManager()