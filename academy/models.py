from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    post = models.TextField()
    user_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + " "+ self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    comment = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
