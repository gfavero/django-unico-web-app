# Generated by Django 3.2.13 on 2022-06-27 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members_app', '0002_rename_user_autorized_profile_user_authorized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
