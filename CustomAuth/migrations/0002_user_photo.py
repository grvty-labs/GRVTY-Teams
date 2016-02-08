# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(max_length=255, upload_to=b'user_pics', null=True, verbose_name=b'Foto de Perfil', blank=True),
        ),
    ]
