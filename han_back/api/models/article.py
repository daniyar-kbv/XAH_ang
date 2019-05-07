from django.db import models
from django.contrib.auth.models import User
from .category import Category

from datetime import datetime


class ArticleManager(models.Manager):
    def for_category(self, category):
        return self.filter(category=category)


class Article(models.Model):
    title = models.CharField(max_length=512)
    body = models.CharField(max_length=1024)
    imageUrl = models.CharField(max_length=512)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    objects = ArticleManager()