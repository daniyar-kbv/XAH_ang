from django.db import models
from .article import Article
from django.contrib.auth.models import User

class ArticleLike(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)