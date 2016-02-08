from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

from solo.models import SingletonModel

SITE_NAME = getattr(settings, 'SITE_NAME', '')

class Configuration(SingletonModel):
    # General Variables
    site_url = models.URLField(_('Main Site URL'), max_length=255, blank=True)
    twitter_username = models.CharField(_('Twitter Username'), max_length=255, blank=True)
    welcome_video_embed = models.TextField(_('Welcome Video'), blank=True)

    class Meta:
        verbose_name = _('%s Configuration' % SITE_NAME)
        verbose_name_plural = _('%s Configuration' % SITE_NAME)

    def __unicode__(self):
        return u'%s' % _('%s Configuration' % SITE_NAME)
