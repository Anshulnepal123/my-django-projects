# Create your models here.
# blog/models.py
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    

    def __str__(self):
        return self.title
    
class Login(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    pw = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

