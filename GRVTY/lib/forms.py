from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms import CharField
from django import forms
import re


email_separator_re = re.compile(r'[^\w\.\-\+@_]+')

def _is_valid_email(email):
    try:
        validate_email(email)
        return True
    except:
        pass
    return False


class EmailsListField(CharField):

    def clean(self, value):
        value = super(EmailsListField, self).clean(value)
        try:
            emails = email_separator_re.split(value.lower())
        except:
            emails = ''
        if not emails:
            raise ValidationError('You should write at least one email.')
        for email in emails:
            if email == '':
                pass
            elif not _is_valid_email(email):
                raise ValidationError("%s it's not a valid email." % email)
        return emails
