from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.html import format_html
from django import forms

from GRVTY.lib.forms import EmailsListField
from GRVTY.lib.images import crop_image
from GRVTY.lib.email import send_mail
from .models import User, Team


class UserCreationAdminForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'invalid_username': _('This is not a valid username.'),
        'duplicate_username': _('A user with that username already exists.'),
        'duplicate_email': _('A user with that email already exists.'),
        'password_mismatch': _('The two password fields didn\'t match.'),
    }
    email = forms.EmailField(label=_('Email'), required=True)
    password1 = forms.CharField(label=_('Password'),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'),
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User._default_manager.get(email__iexact=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        aux = username.replace('user_', '')
        if username.startswith('user_') and aux.isdigit() and int(aux) != self.instance.pk:
            raise forms.ValidationError(
                self.error_messages['invalid_username'],
                code='invalid_username',
            )
        try:
            User._default_manager.exclude(id=self.instance.id).get(username__iexact=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def save(self, commit=True):
        user = super(UserCreationAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeAdminForm(forms.ModelForm):
    email = forms.EmailField(label=_('Email'), required=True)
    username = forms.RegexField(label=_('Username'), max_length=30, regex=r'^[\w.@+-]+$')
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeAdminForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User._default_manager.exclude(id=self.instance.id).get(email__iexact=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        aux = username.replace('user_', '')
        if username.startswith('user_') and aux.isdigit() and int(aux) != self.instance.pk:
            raise forms.ValidationError(
                self.error_messages['invalid_username'],
                code='invalid_username',
            )
        try:
            User._default_manager.exclude(id=self.instance.id).get(username__iexact=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial['password']

class UserCreationForm(UserCreationAdminForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs = {'class': 'form-control'}

class UserEditForm(UserChangeAdminForm):

    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        try:
            del(self.fields['password'])
            del(self.fields['username'])
        except:
            pass
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs = {'class': 'form-control'}
        self.fields['image'].required = False

    def save(self, *args, **kwargs):
        instance = super(UserEditForm, self).save(*args, **kwargs)
        try:
            crop_image(instance.image.path)
        except:
            pass
        return instance


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label=_('Email'), max_length=254)

    def save(self, domain_override=None,
             subject_template_name='emails/forgot_password_subject.txt',
             email_template_name='emails/forgot_password.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        email = self.cleaned_data['email'].strip()
        active_users = User._default_manager.filter(
            email__iexact=email, is_active=True
        )
        for user in active_users:
            if not user.has_usable_password():
                continue
            c = {
                'email': user.email,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
            }
            send_mail('forgot_password', [user.email], context=c)


class InterfaceForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('menubar_fold', )


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name',)


class InviteTeamMateForm(forms.Form):
    emails = EmailsListField()
