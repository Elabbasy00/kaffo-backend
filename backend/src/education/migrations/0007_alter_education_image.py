# Generated by Django 4.2.8 on 2024-03-30 17:16

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_alter_education_image_alter_educationstage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[500, 500], upload_to='stage/'),
        ),
    ]
