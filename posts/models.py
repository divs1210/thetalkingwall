from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author    = models.ForeignKey(User)
    post_text = models.CharField(max_length=1000)
    pub_date  = models.DateTimeField('date published')
    upvotes   = models.IntegerField(default=0)

class Comment(models.Model):
    author       = models.ForeignKey(User)
    post         = models.ForeignKey(Post)
    comment_text = models.CharField(max_length=1000)
    upvotes      = models.IntegerField(default=0)
