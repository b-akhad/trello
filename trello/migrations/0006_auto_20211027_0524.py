# Generated by Django 3.2.8 on 2021-10-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0005_alter_newuser_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='NewUser',
        ),
    ]
