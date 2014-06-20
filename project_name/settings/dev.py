from .base import *

SECRET_KEY = 'dev_{{ secret_key }}'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS += ('debug_toolbar', )

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    },
}


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'user@domain.tld'
EMAIL_HOST_PASSWORD = 'passw0rd'
EMAIL_PORT = 587
