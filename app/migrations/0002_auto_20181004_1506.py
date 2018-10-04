# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-04 12:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', tinymce.models.HTMLField(blank=True)),
                ('post_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Comment'),
        ),
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Like'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.Image'),
        ),
    ]