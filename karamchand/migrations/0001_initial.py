# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeker_email', models.CharField(max_length=64)),
                ('entity', models.CharField(max_length=128)),
                ('address1', models.CharField(blank=True, max_length=128)),
                ('address2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('zip', models.CharField(blank=True, max_length=10)),
                ('state', models.CharField(blank=True, max_length=64)),
                ('country', models.CharField(blank=True, max_length=64)),
                ('website', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]