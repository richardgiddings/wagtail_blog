from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!ln0=bd(fyls_iglj7n((9==s3i9h=p#44+bl5inlbiww-95ht'


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'howto_project_db',
        'USER': 'postgres',
    }
}

ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass
