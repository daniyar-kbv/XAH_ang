from django.db import models
from django.contrib.auth.models import User
from .comment import Comment

# class CommentLikeManager(models.Manager):
#     def for_user(self, user):
#         return self.filter(owner=user)

class CommentLike(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='commentLikes', default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}: {}'.format(self.id, self.comment_id)

    def to_json(self):
        return {
            'id': self.id,
            'comment': self.comment_id
        }
