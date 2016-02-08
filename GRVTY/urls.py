from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
import re

admin.autodiscover()

urlpatterns = [
    # Index view
    url(r'^$', 'GRVTY.views.index'),
    # Admin Site URLs
    url(r'^admin/', include(admin.site.urls)),
    # CustomAuth URLs
    url(r'^', include('CustomAuth.urls', app_name='CustomAuth', namespace='Auth')),
    # CustomAuth URLs
    url(r'^', include('Identity.urls', app_name='Identity', namespace='Identity')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    ]
