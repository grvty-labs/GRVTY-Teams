from django.utils.translation import ugettext_lazy as _
from django.templatetags.static import static
from django.conf import settings
from django.db import models

from .utils import demographic


class Persona(models.Model):
    # Permission Data
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Owner'), related_name='personas')
    # Background
    name = models.CharField(_('Name'), max_length=255, blank=True)
    photo = models.ImageField(_('Photo'), upload_to='persona_photos', blank=True)
    gender = models.CharField(_('Gender'), max_length=1, choices=demographic.GENDER_CHOICES, blank=True)
    age = models.PositiveSmallIntegerField(_('Age'), blank=True, null=True)
    job_title = models.CharField(_('Job Title'), max_length=255, blank=True)
    main_quote = models.TextField(_('Main Quote'), blank=True)
    work_experience = models.TextField(_('Work Experience'), blank=True)
    # Demographics
    urbanicity = models.PositiveSmallIntegerField(
        _('Location'), choices=demographic.URBANICITY_CHOICES,
        blank=True, null=True
    )
    individual_income = models.PositiveIntegerField(_('Individual Income'), blank=True, null=True)
    household_income = models.PositiveIntegerField(_('Household Income'), blank=True, null=True)
    main_goal = models.TextField(_('Main Goal'), blank=True)
    secondary_goal = models.TextField(_('Secondary Goal'), blank=True)
    biggest_pain = models.CharField(_('Biggest Pain'), max_length=255, blank=True)
    decrease_pain = models.CharField(_('Decrease Pain'), max_length=255, blank=True)
    biggest_gain = models.CharField(_('Biggest Gain'), max_length=255, blank=True)
    increase_gain = models.CharField(_('Increase Gain'), max_length=255, blank=True)
    identifiers = models.TextField(_('Identifiers'), blank=True, help_text='One per line.')
    communication_preference = models.PositiveSmallIntegerField(
        _('Communication Preference'), choices=demographic.COMMUNICATION_PREFERENCE_CHOICES,
        blank=True, null=True
    )
    objections_barriers = models.TextField(_('Common Objections/Barriers'), blank=True)
    product_pitch = models.TextField(_('Product Pitch'), blank=True)
    triggering_events = models.TextField(_('Triggering Events'), blank=True, help_text='One per line.')
    influencers = models.TextField(_('Influencers'), blank=True, help_text='One per line.')
    funnel = models.TextField(_('First Step in Funnel'), blank=True, help_text='One step per line.')

    class Meta:
        verbose_name_plural = _('Persona')
        verbose_name = _('Personas')

    def __unicode__(self):
        return u'%s' % self.name

    @property
    def individual_income_percentage(self):
        if self.individual_income:
            if self.household_income:
                return int((float(self.individual_income) / self.household_income) * 100)
            return 100
        return 0

    @property
    def household_income_percentage(self):
        return 100 - self.individual_income_percentage

    @property
    def has_pain_or_gain(self):
        arr = [
            self.biggest_pain,
            self.decrease_pain,
            self.biggest_gain,
            self.increase_gain,
        ]
        return any(arr)

    @property
    def has_goals(self):
        arr = [
            self.main_goal,
            self.secondary_goal,
        ]
        return any(arr)

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        return static('photos/gravatar.jpg')

    def get_urbanicity_photo(self):
        if self.urbanicity:
            return static('photos/urbanicity/%d.jpg' % self.urbanicity)
        return ''
