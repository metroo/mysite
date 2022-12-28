from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import EmbedContent
from django.contrib import messages
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
                newslug = obj.slug
                Permission.objects.filter(codename=lastslug.get('slug'), content_type_id=id).delete()
                vote_count = Permission.objects.filter(codename=newslug).count()
                #print(vote_count)
                if(vote_count==0):
                    permission = Permission.objects.create(
                        codename=obj.slug,
                        name=obj.title,
                        content_type=content_type,
                    )
                else:
                    return self.message_user(request, 'Error : Slug was not Uniq', messages.ERROR)
        except:
            return self.message_user(request, 'Slug was not Uniq', messages.ERROR)
        #finally:
        super(EmbedContentAdmin, self).save_model(request, obj, form, change)