from django.conf import settings as dj_settings
from django import template

register = template.Library()

@register.filter(name='split_lines')
def split_lines(text):
    try:
        return text.splitlines()
    except:
        return [text]
