# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-26 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=100)),
                ('datetime', models.DateField()),
            ],
        ),
    ]
