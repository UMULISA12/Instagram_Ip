# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]