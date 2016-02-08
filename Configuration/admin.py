from solo.admin import SingletonModelAdmin
from django.contrib import admin

import Configuration.models

admin.site.register(Configuration.models.Configuration, SingletonModelAdmin)
