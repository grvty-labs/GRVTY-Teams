from django.core.mail import EmailMessage
from django.template import loader
from django.conf import settings

from Configuration.models import Configuration


def send_mail(template_name, recipients, context={}):
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', '')
    default_context = {
        'site_name': getattr(settings, 'SITE_NAME', ''),
        'domain': getattr(settings, 'DOMAIN_NAME', '').rstrip('/'),
        'protocol': 'https' if getattr(settings, 'USE_HTTPS', False) else 'http',
        'CONFIGURATION': Configuration.objects.get(),
    }
    context.update(default_context)
    subject = loader.render_to_string('emails/' + template_name + '_subject.txt', context)
    subject = ''.join(subject.splitlines())
    email_content = loader.render_to_string('emails/' + template_name + '.html', context)
    email_message = EmailMessage(subject, email_content, from_email, recipients)
    email_message.content_subtype = "html"  # Main content is now text/html
    email_message.send(fail_silently=True)
