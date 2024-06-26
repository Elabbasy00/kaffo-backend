# Generated by Django 4.2.8 on 2024-03-30 14:04

import ckeditor_uploader.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=1, scale=None, size=[500, 300], upload_to='blog/cover/')),
                ('overview', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
    ]
