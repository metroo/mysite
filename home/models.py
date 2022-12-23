from django.db import models
from django.contrib import admin

# Create your models here.
class Todo(models.Model):

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned") ,)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return self.title
