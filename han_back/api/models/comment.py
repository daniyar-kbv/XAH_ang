from django.db import models
from django.contrib.auth.models import User
from .article import Article
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


class CommentArticleManager(models.Manager):
    def get_queryset(self, article_id):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        return super().get_queryset().filter(article=article)


class Comment(models.Model):
    body = models.CharField(max_length=255)
    date_published = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    comments_by_article = CommentArticleManager()