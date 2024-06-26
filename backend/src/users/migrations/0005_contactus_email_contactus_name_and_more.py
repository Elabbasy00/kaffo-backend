# Generated by Django 4.2.8 on 2024-03-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='ahmedelabbasy5@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='ahmed', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(default='201062347769', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='services',
            field=models.CharField(default='null', max_length=300),
            preserve_default=False,
        ),
    ]
