"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# END EMAIL CONFIGURATION


# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "testdb",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": "localhost",
        "PORT": "",
    }
}

# END DATABASE CONFIGURATION


# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION


# graphene_django CONFIGURATION

INSTALLED_APPS += (
    'graphene_django',

)

MIDDLEWARE_CLASSES += (
    
)

GRAPHENE = {
    'SCHEMA': 'api.schema.schema' # Where your Graphene schema lives
}
# END graphene_django CONFIGURATION

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
# END TOOLBAR CONFIGURATION


# ######## Override Loggin path
# Override
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        # Log to a text file that can be rotated by logrotate
        # the log path should be generated before run
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'simple',
            'filename': normpath(join(SITE_ROOT, '..',
                                      'var', 'log',  'django',
                                      'myapp.log')),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        # 'myapp': {
        #     'handlers': ['logfile'],
        #     'level': 'WARNING',  # Or maybe INFO or DEBUG
        #     'propagate': False
        # },

    },

}
