from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import EmbedContent
from django.db import transaction

# Register your models here.
@admin.register(EmbedContent)
class EmbedContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'url' , 'published')
    search_fields = ('title', 'url')
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        content_type = ContentType.objects.get_for_model(EmbedContent)
        try:
            if 'slug' in  form.changed_data:
                id = content_type.id
                lastslug = form.initial
                print(lastslug.get('slug'))
                Permission.objects.filter(codename=lastslug.get('slug'), content_type_id=id).delete()

                permission = Permission.objects.create(
                    codename=obj.slug,
                    name=obj.title,
                    content_type=content_type,
                )
        except:
            pass
        super(EmbedContentAdmin, self).save_model(request, obj, form, change)