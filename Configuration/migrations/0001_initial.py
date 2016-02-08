# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_username', models.CharField(max_length=255, verbose_name='Twitter Username', blank=True)),
            ],
            options={
                'verbose_name': 'GRVTY Configuration',
                'verbose_name_plural': 'GRVTY Configuration',
            },
        ),
    ]
