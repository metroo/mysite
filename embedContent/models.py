from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class EmbedContent(models.Model):

    title = models.CharField(max_length=200 , verbose_name=_('title'))
    url = models.CharField(max_length=500 ,verbose_name=_('url'))
    imageurl = models.ImageField()
    published = models.BooleanField()
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'داشبورد'
        verbose_name_plural = 'لیست داشبوردها'