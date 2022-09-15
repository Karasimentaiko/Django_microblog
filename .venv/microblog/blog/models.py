from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=225)
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)