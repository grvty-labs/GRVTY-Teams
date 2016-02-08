from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import PermissionDenied
from django.forms.models import modelform_factory
from django.http import Http404, HttpResponse
from django.contrib.auth import get_user_model

from CustomAuth.forms import UserEditForm
from .models import *
from .utils import demographic
from .forms import InviteFriendsForm, PersonaForm
from GRVTY.lib.email import send_mail


User = get_user_model()


@login_required
@csrf_exempt
def welcome(request):
    if request.user.complete_profile:
        raise Http404
    title = _('Welcome')
    request.session['first_login'] = False
    user = request.user
    form = UserEditForm(instance=user)
    invite_form = InviteFriendsForm()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        value = request.POST.get('value', '')
        if name not in ['first_name', 'last_name', 'email']:
            return HttpResponse('Error', status=400)
        if value:
            setattr(user, name, value)
            user.save()
        return HttpResponse('OK', status=200)
    return TemplateResponse(request, 'identity/welcome/welcome.html', locals())


@login_required
def help(request):
    title = _('Help')
    return TemplateResponse(request, 'identity/help.html', locals())


@login_required
def invite_friends(request):
    form = InviteFriendsForm(request.POST or None)
    if form.is_valid():
        extra_context = {
            'user': request.user
        }
        emails = form.cleaned_data['emails']
        aux = User.objects.filter(email__in=emails).values_list('email', flat=True)
        emails = list(set(emails) - set(aux))
        send_mail('invite_friends', emails, extra_context)
        return HttpResponse('OK', status=200)
    return TemplateResponse(request, 'identity/welcome/invite_friends_form.html', locals())


@login_required
def list_personas(request):
    title = _('Personas')
    personas_active = True
    qs = request.user.personas.all()
    return TemplateResponse(request, 'identity/persona/list.html', locals())


@login_required
def view_persona(request, persona_id):
    personas_active = True
    title = _('Persona')
    persona = get_object_or_404(Persona, id=persona_id, owner=request.user)
    DEMOGRAPHIC = demographic
    return TemplateResponse(request, 'identity/persona/view.html', locals())


@login_required
def add_edit_persona(request, persona_id=None):
    personas_active = True
    title = _('Persona')
    persona = Persona()
    if persona_id:
        persona = get_object_or_404(Persona, id=persona_id, owner=request.user)
    form = PersonaForm(request.POST or None, request.FILES or None, instance=persona)
    if form.is_valid():
        if not persona_id:
            form.instance.owner = request.user
        persona = form.save()
        return redirect('Identity:view_persona', persona.id)
    return TemplateResponse(request, 'identity/persona/form.html', locals())

@login_required
def delete_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id, owner=request.user)
    persona.delete()
    return redirect('Identity:personas')
