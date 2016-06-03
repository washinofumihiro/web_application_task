# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='page',
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=255, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.TextField(blank=True, verbose_name='内容'),
        ),
    ]
