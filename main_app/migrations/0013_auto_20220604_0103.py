# Generated by Django 3.2.13 on 2022-06-04 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0012_rename_author_base_table_author_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base_table_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_base', models.TextField(blank=True, max_length=255)),
                ('author_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('content_conjunto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.conjunto_table')),
            ],
        ),
        migrations.DeleteModel(
            name='Base_table',
        ),
    ]