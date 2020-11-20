from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    images=models.ImageField(upload_to='images/',blank=True)
    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField(max_length=3000,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)