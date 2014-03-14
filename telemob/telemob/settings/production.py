# coding: utf-8
import ConfigParser
import os

from .base import *

OPT_DJANGO_CONF_APP = '/opt/django/configs/apps/{{ project_name }}.conf'
CONF_FILE_EXISTS = os.path.exists(OPT_DJANGO_CONF_APP)


def read_config_file():
    '''
    tenta ler arquivo de configuração
    Return: objeto do tipo ConfigParser
    '''
    config = ConfigParser.ConfigParser()
    config_file = None
    try:
        config_file = open(OPT_DJANGO_CONF_APP)
    except IOError as e:
        raise Exception(u"I/O error({0}): {1} - Possível arquivo inexistente.".format(e.errno, e.strerror))
    except:
        raise Exception(u"Erro não esperado:", sys.exc_info()[0])

    config.readfp(config_file)

    return config

if CONF_FILE_EXISTS:
    config = read_config_file()
    SECRET_KEY = config.get('APP', 'secret_key')


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
