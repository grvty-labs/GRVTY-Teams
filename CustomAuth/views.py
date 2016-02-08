# -*- coding: utf-8 -*-
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.views import login as dj_login
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.core.exceptions import PermissionDenied
from django.forms.models import modelform_factory
from django.core.urlresolvers import reverse
from django.db.models import Prefetch
from django.http import HttpResponse

from GRVTY.lib.images import crop_image
from CustomAuth.models import TeamInvitation
from CustomAuth.forms import *

from datetime import datetime
import json

from django.contrib.auth import get_user_model
User = get_user_model()

ImageForm = modelform_factory(User, fields=('image', ))


# SignUp
def sign_up(request):
    title = _('Sign up')
    next_page = request.GET.get('next', '')
    if request.user.is_authenticated():
        auth_logout(request)
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.backend = 'CustomAuth.backends.EmailOrUsernameModelBackend'
        auth_login(request, user)
        if next_page:
            return redirect(next_page)
        return redirect('/')
    return TemplateResponse(request, 'auth/signup.html', locals())


# Login
def custom_login(request):
    title = _('Log in')
    if request.user.is_authenticated():
        return redirect('/')
    return dj_login(request, template_name='auth/login.html', extra_context={'title':title})


def claim_invitation(request, uuid_code):
    title = _('Invitation')
    invitation = get_object_or_404(TeamInvitation.objects.select_related('team'), uuid_code=uuid_code)
    if request.user.is_authenticated() and request.method == 'POST':
        if invitation.claimed:
            raise PermissionDenied
        invitation.redeemer = request.user
        invitation.claimed = True
        invitation.redeemed_on = datetime.now()
        invitation.save()
        if request.user.id != invitation.team.owner_id:
            invitation.team.members.add(request.user)
        return redirect('Auth:team_view', invitation.team_id)
    return TemplateResponse(request, 'account/teams/clain_invitation.html', locals())


# Verification
def verify_email(request, uuid_code):
    title = 'Verify Email'
    user = get_object_or_404(User, verification_code=uuid_code, verified=False)
    user.verified = True
    user.save()
    return TemplateResponse(request, 'auth/verified.html', locals())


@login_required
def resend_verification_email(request):
    request.user.send_verification_email()
    return redirect('/')


# Account
@login_required
def profile(request):
    title = _('Profile')
    user = request.user
    form = UserEditForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        user = form.save()
        return redirect('/')
    return TemplateResponse(request, 'account/profile.html', locals())


# Interface Data
@login_required
def interface_data(request):
    form = InterfaceForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return HttpResponse('OK', status=200)
    return HttpResponse('ERROR', status=400)


# API
@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.instance.complete_profile = True
            user = form.save()
            try:
                crop_image(user.image.path)
            except:
                pass
            return HttpResponse('%s' % user.get_photo_url(), status=200)
    return HttpResponse('ERROR', status=400)


@login_required
def complete_profile(request):
    if request.method != 'GET':
        return HttpResponse('ERROR', status=400)
    user = request.user
    if not user.complete_profile:
        user.complete_profile = True
        user.save()
    return HttpResponse('OK', status=200)


# Teams
@login_required
def teams(request):
    teams_active = True
    title = _('Teams')
    teams = request.user.teams.select_related('owner').prefetch_related('members').all() | request.user.created_teams.prefetch_related('members').all()
    teams = teams.distinct()
    new_team_form = TeamForm()
    return TemplateResponse(request, 'account/teams/list.html', locals())


@login_required
def team_add_edit(request, team_id=None):
    if not request.is_ajax():
        raise PermissionDenied
    instance = Team()
    if team_id:
        instance = get_object_or_404(Team, id=team_id, owner=request.user)
    form = TeamForm(request.POST or None, instance=instance)
    if form.is_valid():
        if not instance.id:
            form.instance.owner = request.user
        team = form.save()
        data = {
            'status': 'OK',
            'text': team.name,
            'redirect_url': reverse('Auth:team_view', args=[team.id])
        }
        return HttpResponse(json.dumps(data), status=200)
    return TemplateResponse(request, 'account/teams/form.html', locals())


@login_required
def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id, owner=request.user)
    team.delete()
    return redirect('Auth:teams')


@login_required
def team_remove_member(request, team_id):
    team = get_object_or_404(Team, id=team_id, owner=request.user)
    member_id = request.GET.get('member_id', None)
    if member_id and member_id.isdigit():
        team.members.remove(int(member_id))
    return redirect('Auth:team_view', team_id)


@login_required
def team_invite_member(request, team_id):
    team = get_object_or_404(
        Team.objects.select_related('owner').prefetch_related('members'),
        id=team_id,
    )
    if request.user != team.owner and not request.user in team.members.all():
        raise PermissionDenied
    form = InviteTeamMateForm(request.POST or None)
    if form.is_valid():
        emails = form.cleaned_data['emails']
        emails = list(set(emails))
        for email in emails:
            members_emails = [m_email.lower() for m_email in team.members.values_list('email', flat=True)]
            if email not in members_emails:
                try:
                    TeamInvitation.objects.create(team=team, sender=request.user, email=email)
                except:
                    pass
        return HttpResponse('OK', status=200)
    return TemplateResponse(request, 'account/teams/invite_teammates_form.html', locals())


@login_required
def cancel_invitation(request, invitation_id):
    invitation = get_object_or_404(
        TeamInvitation.objects.select_related('team').prefetch_related('team__members'),
        pk=invitation_id, claimed=False,
    )
    team = invitation.team
    if team.owner != request.user and not request.user in team.members.all():
        raise PermissionDenied
    invitation.delete()
    return redirect('Auth:team_view', team.id)


@login_required
def team_view(request, team_id):
    teams_active = True
    title = _('Teams')
    team = get_object_or_404(
        Team.objects.select_related('owner').prefetch_related(
            'members',
            Prefetch('invitations', queryset=TeamInvitation.objects.filter(claimed=False), to_attr='pending_invitations'),
        ),
        id=team_id,
    )
    if request.user != team.owner and not request.user in team.members.all():
        raise PermissionDenied
    if request.user == team.owner:
        edit_team_form = TeamForm(None, instance=team)
    invite_form = InviteTeamMateForm()
    return TemplateResponse(request, 'account/teams/view.html', locals())
