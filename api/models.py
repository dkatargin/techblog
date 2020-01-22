from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=250)


class Entity(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tags)
