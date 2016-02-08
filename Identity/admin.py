from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps


myapp = apps.get_app_config('Identity')
for model in myapp.get_models(include_auto_created=False):
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
