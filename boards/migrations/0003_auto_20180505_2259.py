# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-05 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20180503_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='answercomment',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='questioncomment',
            options={'ordering': ('created_at',)},
        ),
        migrations.AddField(
            model_name='board',
            name='questions_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='users_count',
            field=models.IntegerField(default=0),
        ),
    ]
