# Generated by Django 3.1.1 on 2020-09-12 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_remove_photo_save_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='active',
        ),
        migrations.RemoveField(
            model_name='save',
            name='active',
        ),
    ]
