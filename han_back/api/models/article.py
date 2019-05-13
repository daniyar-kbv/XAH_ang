from django.db import models
from django.contrib.auth.models import User
from .category import Category

from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=512)
    body = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=512)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)
