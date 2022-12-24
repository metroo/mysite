from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import EmbedContent
# Register your models here.

@admin.register(EmbedContent)
class EmbedContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'url' , 'published')
    search_fields = ('title', 'url')
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        try:
            if(form.changed_data.index('slug')):
                content_type = ContentType.objects.get_for_model(EmbedContent)
                Permission.objects.filter(codename=form.initial.slug)
        except:
            print("not ok")


        # permission = Permission.objects.create(
        #     codename=obj.slug,
        #     name=obj.title,
        #     content_type=content_type,
        # )
        super().save_model(request, obj, form, change)