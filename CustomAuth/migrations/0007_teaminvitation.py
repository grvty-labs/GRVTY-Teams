# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('CustomAuth', '0006_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamInvitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('claimed', models.BooleanField(default=False, verbose_name='Claimed')),
                ('uuid_code', models.CharField(unique=True, max_length=36, verbose_name='Invitation Code')),
                ('redeemer', models.ForeignKey(related_name='invitations_redeemed', verbose_name='Redeemer', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('sender', models.ForeignKey(related_name='invitations_sent', verbose_name='Sender', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(related_name='invitations', verbose_name='Team', to='CustomAuth.Team')),
            ],
            options={
                'verbose_name': 'Team Invitation',
                'verbose_name_plural': 'Team Invitations',
            },
        ),
    ]
