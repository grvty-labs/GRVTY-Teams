from django.utils.translation import ugettext_lazy as _
from django.conf.urls import patterns, url


urlpatterns = patterns('Identity.views',
    url(r'^welcome/$', 'welcome', name='welcome'),
    url(r'^help/$', 'help', name='help'),
    url(r'^personas/$', 'list_personas', name='personas'),
    url(r'^personas/add/$', 'add_edit_persona', name='add_persona'),
    url(r'^personas/(?P<persona_id>\d+)/edit/$', 'add_edit_persona', name='edit_persona'),
    url(r'^personas/(?P<persona_id>\d+)/delete/$', 'delete_persona', name='delete_persona'),
    url(r'^personas/(?P<persona_id>\d+)/$', 'view_persona', name='view_persona'),
    url(r'^invite-friends/$', 'invite_friends', name='invite_friends'),
)
