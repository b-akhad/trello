# Generated by Django 3.2.8 on 2021-10-29 12:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trello', '0011_alter_phone_profile_picture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phone',
            new_name='Picture',
        ),
    ]
