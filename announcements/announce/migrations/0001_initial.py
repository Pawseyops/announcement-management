# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=1024)),
                ('reference', models.CharField(unique=True, max_length=64)),
                ('body', models.TextField()),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('withdrawn', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('maillist', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('audience', models.ManyToManyField(to='announce.Audience')),
                ('location', models.ForeignKey(to='announce.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Silo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('owner', models.ForeignKey(to='announce.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('html', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='silo',
            field=models.ForeignKey(to='announce.Silo'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='template',
            field=models.ForeignKey(to='announce.Template'),
        ),
    ]
