# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0003_auto_20151130_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='site_url',
            field=models.URLField(max_length=255, verbose_name='Main Site URL', blank=True),
        ),
    ]
