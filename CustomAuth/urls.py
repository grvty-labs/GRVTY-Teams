from django.utils.translation import ugettext_lazy as _
from django.conf.urls import patterns, url
from CustomAuth.forms import PasswordResetForm

urlpatterns = patterns('',
    # Logout Built in View
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {
            'next_page': '/login',
            'extra_context': {'title':_('Log out')}
        },
        name='logout',
    ),
    # Forgot Password
    url(r'^forgot_password/$', 'django.contrib.auth.views.password_reset',
        {
            'template_name': 'auth/forgot_password.html',
            'password_reset_form': PasswordResetForm,
            'subject_template_name': 'emails/forgot_password_subject.txt',
            'email_template_name': 'emails/forgot_password.html',
            'post_reset_redirect' : '/forgot_password/complete/',
            'extra_context': {'title':_('Reset your password')},
        },
        name='forgot_password',
    ),
    url(r'^forgot_password/complete/$', 'django.contrib.auth.views.password_reset_done',
        {
            'template_name':'auth/forgot_password.html',
            'extra_context': {'title':_('Reset password'), 'complete':True}
        },
        name='forgot_password_done'
    ),
    url(r'^reset_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {
            'template_name':'auth/password_reset.html',
            'post_reset_redirect':'/reset_password/complete/',
            'extra_context': {'title':_('Reset password')}
        },
        name='reset_password'
    ),
    url(r'^reset_password/complete/$', 'django.contrib.auth.views.password_reset_complete',
        {
            'template_name':'auth/password_reset.html',
            'extra_context': {'title':_('Reset password complete'), 'complete': True}
        },
        name='reset_password_complete'
    ),
    url(r'^change_password/$', 'django.contrib.auth.views.password_change',
        {
            'template_name': 'auth/change_password.html',
            'post_change_redirect':'/profile'
        },
        name='change_password'
    ),
)


urlpatterns += patterns('CustomAuth.views',
    # Login Views
    url(r'^login/$', 'custom_login', name='login'),
    url(r'^sign_up/$', 'sign_up', name='sign_up'),
    # Verification
    url(r'^verify/resend_email/$', 'resend_verification_email', name='resend_verification_email'),
    url(r'^verify/(?P<uuid_code>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})/$', 'verify_email', name='verify_email'),
    # Account
    url(r'^profile/$', 'profile', name='profile'),
    url(r'^teams/$', 'teams', name='teams'),
    url(r'^teams/add/$', 'team_add_edit', name='team_add'),
    url(r'^teams/(?P<team_id>\d+)/$', 'team_view', name='team_view'),
    url(r'^teams/(?P<team_id>\d+)/edit/$', 'team_add_edit', name='team_edit'),
    url(r'^teams/(?P<team_id>\d+)/delete/$', 'team_delete', name='team_delete'),
    url(r'^teams/(?P<team_id>\d+)/remove_member/$', 'team_remove_member', name='team_remove_member'),
    url(r'^teams/(?P<team_id>\d+)/invite_member/$', 'team_invite_member', name='team_invite_member'),
    url(r'^invitations/(?P<uuid_code>[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})/', 'claim_invitation', name='claim_invitation'),
    url(r'^invitations/(?P<invitation_id>\d+)/delete/', 'cancel_invitation', name='cancel_invitation'),
    # Upload Photo
    url(r'^upload_photo/$', 'upload_photo', name='upload_photo'),
    # Complete Profile
    url(r'^complete_profile/$', 'complete_profile', name='complete_profile'),
    # Interaction Specifices
    url(r'^profile/interface_data/$', 'interface_data', name='interface_data'),
)
