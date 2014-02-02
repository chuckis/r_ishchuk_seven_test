from base import PROJECT_ROOT, SITE_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True


DATABASES = {
 "default": {
     "ENGINE": "django.db.backends.postgresql_psycopg2",
     "NAME": "django_deploy",
     "USER": "postgres",
     "PASSWORD": "postgres",
     "HOST": "localhost",
     "PORT": "5432",
 }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django15.apps.note',
    'django_forms_bootstrap',
)
