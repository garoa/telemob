# coding: utf-8
import os

from .base import *


DJANGO_HOME = os.path.join('/opt', 'django')
STATIC_DIR = os.path.join(DJANGO_HOME, 'static_files', '{{ project_name }}')
MEDIA_ROOT = os.path.join(STATIC_DIR, 'media')
STATIC_ROOT = os.path.join(STATIC_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
