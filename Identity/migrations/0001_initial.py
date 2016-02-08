# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('photo', models.ImageField(upload_to=b'persona_photos', verbose_name='Photo', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female')])),
                ('age', models.PositiveSmallIntegerField(null=True, verbose_name='Age', blank=True)),
                ('urbanicity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Location', choices=[(1, 'Urban'), (2, 'Suburban'), (3, 'Rural'), (4, 'Small Town')])),
                ('job_position', models.CharField(max_length=255, verbose_name='Job Position', blank=True)),
                ('work_experience', models.TextField(verbose_name='Work Experience', blank=True)),
                ('main_quote', models.TextField(verbose_name='Main Quote', blank=True)),
                ('individual_income', models.PositiveIntegerField(null=True, verbose_name='Individual Income', blank=True)),
                ('household_income', models.PositiveIntegerField(null=True, verbose_name='Household Income', blank=True)),
                ('main_goal', models.TextField(verbose_name='Main Goal', blank=True)),
                ('secondary_goal', models.TextField(verbose_name='Secondary Goal', blank=True)),
                ('main_challenge', models.TextField(verbose_name='Main Challenge', blank=True)),
                ('secondary_challenge', models.TextField(verbose_name='Secondary Challenge', blank=True)),
                ('biggest_pain', models.CharField(max_length=255, verbose_name='Biggest Pain', blank=True)),
                ('decrease_pain', models.CharField(max_length=255, verbose_name='Decrease Pain', blank=True)),
                ('biggest_gain', models.CharField(max_length=255, verbose_name='Biggest Gain', blank=True)),
                ('increase_pain', models.CharField(max_length=255, verbose_name='Increase Gain', blank=True)),
                ('identifiers', models.TextField(verbose_name='Identifiers', blank=True)),
                ('communication_preference', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Communication Preference', choices=[(1, 'Email'), (2, 'Telephone')])),
                ('objections_barriers', models.TextField(verbose_name='Common Objections/Barriers', blank=True)),
                ('product_pitch', models.TextField(verbose_name='Product Pitch', blank=True)),
                ('triggering_events', models.TextField(verbose_name='Triggering Events', blank=True)),
                ('influencers', models.TextField(verbose_name='Influencers', blank=True)),
                ('funnel', models.TextField(verbose_name='First Step in Funnel', blank=True)),
                ('owner', models.ForeignKey(related_name='personas', verbose_name='Owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Personas',
                'verbose_name_plural': 'Persona',
            },
        ),
    ]
