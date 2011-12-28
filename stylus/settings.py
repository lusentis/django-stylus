import os

from django.conf import settings as django_settings

""" default directories """
STYLUS_ROOT = getattr(django_settings, 'STYLUS_ROOT', os.path.join(getattr(django_settings, 'STATIC_ROOT'),'_css'))
STYLUS_OUTPUT_DIR = getattr(django_settings, 'STYLUS_OUTPUT_DIR', 'compiled')
STYLUS_SYS_OUTPUT_DIR = os.path.join(STYLUS_ROOT, STYLUS_OUTPUT_DIR)
STYLUS_URL = getattr(django_settings, 'STYLUS_URL', ''.join([getattr(django_settings, 'STATIC_URL'), '_css/', STYLUS_OUTPUT_DIR]))

""" stylus cache time """
STYLUS_CACHE_TIME = getattr(django_settings, 'STYLUS_CACHE_TIME', 60*60)

""" stylus executable settings """
STYLUS_BIN = getattr(django_settings, 'STYLUS_BIN', 'stylus')
STYLUS_PARAMS = '' #getattr(django_settings, 'STYLUS_PARAMS', ' -c -f -l --inline ')

""" make output directories """
try:
    os.makedirs(STYLUS_SYS_OUTPUT_DIR)
except OSError:
    pass

