# Generated by Django 4.1.2 on 2022-12-24 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('embedContent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='embedcontet',
            old_name='sulg',
            new_name='slug',
        ),
    ]
