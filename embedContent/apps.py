from django.apps import AppConfig
from django.db.models.signals import pre_save


class EmbedcontentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'embedContent'
    verbose_name = "داشبورد ها"

