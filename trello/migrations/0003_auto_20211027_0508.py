# Generated by Django 3.2.8 on 2021-10-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0002_alter_newuser_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterModelOptions(
            name='newuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='newuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='username',
        ),
        migrations.AlterModelTable(
            name='newuser',
            table='auth_employee',
        ),
    ]