from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    author = models.CharField(max_length=155)
    publication_date = models.DateTimeField(auto_now_add=True)