# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docker_containers',
            name='command',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docker_containers',
            name='created',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docker_containers',
            name='ports',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docker_containers',
            name='status',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docker_images',
            name='created',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='docker_images',
            name='size',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server',
            name='cpu_info',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server',
            name='disk_info',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server',
            name='memory_info',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
