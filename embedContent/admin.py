from django.contrib import admin
from .models import embedContet
# Register your models here.

@admin.register(embedContet)
class EmbedContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'url' , 'published')
    search_fields = ('title', 'url')
    prepopulated_fields = {'slug': ('title',)}