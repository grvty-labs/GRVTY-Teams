from django import forms

from GRVTY.lib.forms import EmailsListField
from GRVTY.lib.images import crop_image
from .models import Persona


class InviteFriendsForm(forms.Form):
    emails = EmailsListField()


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        exclude = ['owner']

    def __init__(self, *agrs, **kwargs):
        super(PersonaForm, self).__init__(*agrs, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            attrs = {'class': 'form-control'}
            if field.help_text:
                attrs['data-hint'] = field.help_text
            field.widget.attrs = attrs
        self.fields['gender'].widget.attrs['data-plugin'] = 'selectpicker'
        self.fields['communication_preference'].widget.attrs['data-plugin'] = 'selectpicker'
        self.fields['urbanicity'].widget.attrs['data-plugin'] = 'selectpicker'

    def save(self, *args, **kwargs):
        instance = super(PersonaForm, self).save(*args, **kwargs)
        try:
            crop_image(self.instance.photo.path)
        except:
            pass
        return instance
