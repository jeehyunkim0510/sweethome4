from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='old_article', null=True)
    # family = models.ForeignKey(Family, on_delete=models.SET_NULL, related_name='articles', null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(max_length=500, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

class NewArticle(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # family = models.ForeignKey(Family, on_delete=models.SET_NULL, related_name='articles', null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(max_length=500, null=True)
    created_at = models.DateField(null=True)
    # 나머지 모델 필드들