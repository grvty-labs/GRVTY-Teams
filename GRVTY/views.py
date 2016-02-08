from django.shortcuts import redirect


def index(request):
    try:
        first_login = request.session['first_login']
    except:
        first_login = True
    if first_login and request.user.is_authenticated() and not request.user.complete_profile:
        return redirect('Identity:welcome')
    return redirect('Identity:personas')
