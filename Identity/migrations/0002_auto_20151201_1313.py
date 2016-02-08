# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Identity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='job_position',
        ),
        migrations.AddField(
            model_name='persona',
            name='job_title',
            field=models.CharField(max_length=255, verbose_name='Job Title', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name', blank=True),
        ),
    ]
