# Generated by Django 4.1.4 on 2022-12-24 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embedContent', '0002_rename_sulg_embedcontet_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='embedContet',
            new_name='EmbedContent',
        ),
    ]
