# Generated by Django 4.2 on 2023-05-17 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]