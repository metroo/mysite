from django.db import models
from django.contrib import admin

# Create your models here.
class EmbedContent(models.Model):

    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    imageurl = models.ImageField()
    published = models.BooleanField()
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title