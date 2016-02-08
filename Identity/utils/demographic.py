from django.utils.translation import ugettext_lazy as _


# Gender
MALE = 'M'
FEMALE = 'F'

GENDER_CHOICES = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)


# Urbanicity
URBAN = 1
SUBURBAN = 2
RURAL = 3
SMALL_TOWN = 4


URBANICITY_CHOICES = (
    (URBAN, _('Urban')),
    (SUBURBAN, _('Suburban')),
    (RURAL, _('Rural')),
    (SMALL_TOWN, _('Small Town')),
)

# Communication Preference
EMAIL = 1
TELEPHONE = 2

COMMUNICATION_PREFERENCE_CHOICES = (
    (EMAIL, _('Email')),
    (TELEPHONE, _('Telephone')),
)
