# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0005_user_menubar_fold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('members', models.ManyToManyField(related_name='teams', verbose_name='Members', to=settings.AUTH_USER_MODEL, blank=True)),
                ('owner', models.ForeignKey(related_name='created_teams', verbose_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
