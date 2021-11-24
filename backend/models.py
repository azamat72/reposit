from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='images/', default = "images/default.png")

    def get_absolute_url(self):
        return reverse("blog:single", args=[self.slug])

    def __str__(self):
        return self.slug


class Lead(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='images/', default = "images/default.png")


    def get_absolute_url(self):
        return reverse("blog:double", args=[self.slug])

    def __str__(self):
        return self.slug


    