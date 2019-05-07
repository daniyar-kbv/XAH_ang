from django.db import models
from django.contrib.auth.models import User
from .article import Article
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


class CommentManager(models.Manager):

    def comments_article(self, article_id):
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        return super(CommentManager, self).get_queryset().filter(article=article)


class Comment(models.Model):
    body = models.CharField(max_length=255)
    date_published = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)

    # objects = models.Manager
    # comments_by_article = CommentManager()
    objects = CommentManager()

    def __str__(self):
        return self.body
