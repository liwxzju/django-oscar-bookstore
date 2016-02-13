# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 22:13
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='BookFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('virtual', models.BooleanField(default=False, verbose_name='Virtual')),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name_plural': 'book formats',
                'verbose_name': 'book format',
            },
        ),
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name_plural': 'book stores',
                'verbose_name': 'book store',
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name_plural': 'series',
            },
        ),
    ]