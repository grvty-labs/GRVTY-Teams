from django.conf import settings as dj_settings
from django import template

register = template.Library()

@register.filter(name='settings')
def settings(attribute):
    return getattr(dj_settings, attribute, '')


@register.filter(name='no_slash')
def no_slash(string):
    return string.rstrip('/')
