from django.contrib import admin
from .models import Todo
# Register your models here.

@admin.display(description='نام')
def title(self):
    return self.title

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (title , 'body', 'created')
    search_fields = ('title', 'body')


