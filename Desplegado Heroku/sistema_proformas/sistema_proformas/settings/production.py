from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['proformas.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfi8gbnq0bmhdp',
        'USER': 'lnfzveujjecxfm',
        'PASSWORD': '7c03c12f08e708bb570b35605eca01ab444b2a09b2b8813e2eb88caf99f6bcd6',
        'HOST': 'ec2-54-224-120-186.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')