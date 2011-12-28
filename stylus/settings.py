import os

from django.conf import settings as django_settings

""" default directories """
STYLUS_ROOT = getattr(django_settings, 'STYLUS_ROOT', getattr(django_settings, os.path.join('STATIC_ROOT','_css')))
STYLUS_OUTPUT_DIR = os.path.join(STYLUS_ROOT, getattr(django_settings, 'STYLUS_OUTPUT_DIR', 'compiled'))

""" stylus cache time """
STYLUS_CACHE_TIME = getattr(django_settings, 'STYLUS_CACHE_TIME', 60*60)

""" stylus executable settings """
STYLUS_BIN = getattr(django_settings, 'STYLUS_BIN', 'stylus')
STYLUS_PARAMS = getattr(django_settings, 'STYLUS_PARAMS', '')

""" make output directories """
os.makedirs(STYLUS_OUTPUT_DIR)

