from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=128)