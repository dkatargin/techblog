from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Entity(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
