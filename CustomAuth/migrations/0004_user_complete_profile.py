# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0003_auto_20151201_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='complete_profile',
            field=models.BooleanField(default=False, verbose_name='Complete Profile'),
        ),
    ]
