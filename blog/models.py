from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    author = models.ForeignKey(User,models.CASCADE,default=User.objects.get(pk=1).id)