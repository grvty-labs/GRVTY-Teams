# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0002_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(max_length=255, upload_to=b'user_pics', null=True, verbose_name='Profile Image', blank=True),
        ),
    ]
