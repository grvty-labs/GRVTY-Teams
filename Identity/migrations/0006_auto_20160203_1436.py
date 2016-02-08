# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Identity', '0005_auto_20160106_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='funnel',
            field=models.TextField(blank=True, help_text='One step per line.', verbose_name='First Step in Funnel'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='gender',
            field=models.CharField(max_length=1, blank=True, choices=[('M', 'Male'), ('F', 'Female')], verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='identifiers',
            field=models.TextField(blank=True, help_text='One per line.', verbose_name='Identifiers'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='influencers',
            field=models.TextField(blank=True, help_text='One per line.', verbose_name='Influencers'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='photo',
            field=models.ImageField(blank=True, verbose_name='Photo', upload_to='persona_photos'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='triggering_events',
            field=models.TextField(blank=True, help_text='One per line.', verbose_name='Triggering Events'),
        ),
    ]
