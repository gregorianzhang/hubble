# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='docker_containers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('containter_id', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('image', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('command', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('created', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('status', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('ports', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('names', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='docker_images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repository', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('tag', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('image_id', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('created', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('size', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('internet', models.GenericIPAddressField(null=True, protocol=b'IPv4', default=None, blank=True, unique=True)),
                ('intranet', models.GenericIPAddressField(null=True, protocol=b'IPv4', default=None, blank=True, unique=True)),
                ('mac_address', models.CharField(default=None, max_length=17, unique=True, null=True, blank=True)),
                ('host_name', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('cpu_info', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('memory_info', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
                ('disk_info', models.CharField(default=None, max_length=255, unique=True, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
