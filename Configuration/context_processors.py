from .models import Configuration

def configuration_context(request):
    """
    Method that includes Configuration Singleton Object on all templates
    """
    return {
        'CONFIGURATION': Configuration.objects.get()
    }
