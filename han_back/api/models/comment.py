from django.db import models
from django.contrib.auth.models import User


class CommentManager()


class Comment(models.Model):
    body = models.CharField(max_length=255)
    date_published = models.DateField
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # article = models.ForeignKey()