# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0007_teaminvitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminvitation',
            name='redeemed_on',
            field=models.DateTimeField(null=True, verbose_name='Redeemed On', blank=True),
        ),
    ]
