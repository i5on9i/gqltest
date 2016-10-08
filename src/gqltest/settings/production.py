"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# ##### LOAD VARIABLE FROM JSON
# JSON-based secrets module
import json

with open("spike/settings/secret.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = []
########## END HOST CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mydb",    # DB name
        "USER": "django",
        "PASSWORD": get_secret("DB_PW"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
########## END DATABASE CONFIGURATION


# ######### CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#caches
CACHES = {
    'default': {
        # local memory cache
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ######### END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_secret("SECRET_KEY")
# ######### END SECRET CONFIGURATION

# ######### HTTPS CONFIGURATION
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# ######### END HTTPS CONFIGURATION

# ######### ENCRYPT CONFIGURATION
ENCRYPT_PRIVATE_KEY = get_secret("PRIVATE_KEY")
# ENCRYPT_PUBLIC_KEY_PATH = get_secret("PUBLIC_KEY_PATH")
# ######### END ENCRYPT CONFIGURATION
