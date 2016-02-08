# -*- coding: utf-8 -*-
import datetime
import os
DEBUG = True

DEFAULT_FROM_EMAIL = 'GRVTYlabs <server@blacklionlab.com>'
SITE_NAME = 'GRVTYlabs'
DOMAIN_NAME = 'http://192.168.0.105:8000'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# SMTP Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'server@blacklionlab.com'
EMAIL_HOST_PASSWORD = 'd975XBX2#'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Databases
#  SQL Database
USE_SQLITE = True

if not USE_SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',  # Database Name
            'USER': '',  # Database User
            'PASSWORD': '',  # Database User Password
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

# Server Config
ADMINS = (
    # ('Nombre', 'correo@dominio.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['localhost']

# Only for production Mode for apache to serve static and media files
# MEDIA_ROOT = os.path.join()
# MEDIA_URL = ''
# STATIC_ROOT = os.path.join()
# STATIC_URL = ''
