# Generated by Django 3.2.13 on 2022-06-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members_app', '0003_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
