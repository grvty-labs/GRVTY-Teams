# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0004_user_complete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='menubar_fold',
            field=models.BooleanField(default=False, verbose_name='Menubar Fold'),
        ),
    ]
