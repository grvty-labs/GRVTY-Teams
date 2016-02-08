# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0002_initial_config'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuration',
            options={'verbose_name': 'GRVTYlabs Configuration', 'verbose_name_plural': 'GRVTYlabs Configuration'},
        ),
        migrations.AddField(
            model_name='configuration',
            name='welcome_video_embed',
            field=models.TextField(verbose_name='Welcome Video', blank=True),
        ),
    ]
