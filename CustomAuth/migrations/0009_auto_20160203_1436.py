# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0008_teaminvitation_redeemed_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(max_length=255, blank=True, null=True, verbose_name='Profile Image', upload_to='user_pics'),
        ),
    ]
