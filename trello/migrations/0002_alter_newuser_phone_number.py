# Generated by Django 3.2.8 on 2021-10-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]