from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.templatetags.static import static
from django.dispatch import receiver
from django.db import models

from GRVTY.lib.email import send_mail

import shortuuid
import uuid


def get_uuid_code_username():
    short = shortuuid.encode(uuid.uuid1())[:6]
    if short.isdigit():
        return get_uuid_code_username()
    return short


class User(AbstractUser):
    verified = models.BooleanField(_('Verified'), default=False)
    verification_code = models.CharField(_('Verification Code'), max_length=36,
                                         unique=True)
    image = models.ImageField(_('Profile Image'), upload_to='user_pics',
                              max_length=255, blank=True, null=True)
    # Helper Flags
    complete_profile = models.BooleanField(_('Complete Profile'),
                                           default=False)
    menubar_fold = models.BooleanField(_('Menubar Fold'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __unicode__(self):
        return u'%s' % self.username

    @classmethod
    def get_verification_code(cls):
        verification_code = '%s' % uuid.uuid1()
        try:
            cls.objects.get(verification_code=verification_code)
            return cls.get_verification_code()
        except cls.DoesNotExist:
            return verification_code

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_photo_url(self):
        if self.image:
            return self.image.url
        return static('photos/gravatar.jpg')

    def send_verification_email(self):
        if not self.verified:
            c = {
                'email': self.email,
                'user': self,
            }
            send_mail('verify_email', [self.email], context=c)


@receiver(pre_save, sender=User)
def set_tmp_username(sender, **kwargs):
    instance = kwargs['instance']
    if not instance.pk:
        instance.verification_code = sender.get_verification_code()
    if instance.username == '' or (not instance.pk and
                                   instance.username == ''):
        instance.username = 'user_%s' % get_uuid_code_username()
    instance.email = instance.email.strip()
    instance.username = instance.username.strip()


@receiver(post_save, sender=User)
def set_username(sender, **kwargs):
    instance = kwargs['instance']
    save = False
    if instance.id and (instance.username.startswith('user_') and
       not instance.username.replace('user_', '').isdigit()):
        instance.username = 'user_%d' % instance.id
        save = True
    if kwargs['created']:
        c = {
            'email': instance.email,
            'user': instance,
        }
        send_mail('welcome', [instance.email], context=c)
    if save:
        instance.save()


class Team(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    owner = models.ForeignKey('User', related_name='created_teams',
                              verbose_name=_('Owner'))
    members = models.ManyToManyField('User', related_name='teams', blank=True,
                                     verbose_name=_('Members'))

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __unicode__(self):
        return u'%s' % self.name


class TeamInvitation(models.Model):
    team = models.ForeignKey('Team', verbose_name=_('Team'),
                             related_name='invitations')
    sender = models.ForeignKey('User', verbose_name=_('Sender'),
                               related_name='invitations_sent')
    redeemer = models.ForeignKey('User', verbose_name=_('Redeemer'),
                                 related_name='invitations_redeemed',
                                 blank=True, null=True)
    redeemed_on = models.DateTimeField(_('Redeemed On'), blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=255)
    claimed = models.BooleanField(_('Claimed'), default=False)
    uuid_code = models.CharField(_('Invitation Code'), max_length=36,
                                 unique=True)

    class Meta:
        verbose_name = _('Team Invitation')
        verbose_name_plural = _('Team Invitations')

    def __unicode__(self):
        return u'%s' % self.email

    @classmethod
    def get_uuid_code(cls):
        uuid_code = '%s' % uuid.uuid1()
        try:
            cls.objects.get(uuid_code=uuid_code)
            return cls.get_verification_code()
        except cls.DoesNotExist:
            return uuid_code

    def send_mail(self):
        if not self.claimed:
            c = {
                'email': self.email,
                'invitation': self,
            }
            send_mail('team_invitation', [self.email], context=c)


@receiver(pre_save, sender=TeamInvitation)
def set_uuid_code(sender, **kwargs):
    instance = kwargs['instance']
    if not instance.pk:
        instance.uuid_code = sender.get_uuid_code()


@receiver(post_save, sender=TeamInvitation)
def send_invitation_email(sender, **kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        instance.send_mail()
