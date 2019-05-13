from django.db import models
from django.contrib.auth.models import User

# class CategoryManager(models.Manager):
#     def for_user(self, user):
#         return self.filter(owner=user)

class Category(models.Model):
    name = models.CharField('Name',max_length=200)

    def __str__(self):
        return '{}'.format(self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
