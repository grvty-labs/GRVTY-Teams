# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Identity', '0003_auto_20151217_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='increase_pain',
            new_name='increase_gain',
        ),
    ]
