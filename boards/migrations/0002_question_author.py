# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 11:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='asked_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]