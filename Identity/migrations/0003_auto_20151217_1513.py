# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Identity', '0002_auto_20151201_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='gender',
            field=models.CharField(blank=True, max_length=1, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female')]),
        ),
    ]
