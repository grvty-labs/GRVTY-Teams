# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Identity', '0004_auto_20160106_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='main_challenge',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='secondary_challenge',
        ),
    ]
