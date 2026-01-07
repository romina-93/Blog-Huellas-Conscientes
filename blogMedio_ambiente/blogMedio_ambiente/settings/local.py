
from .base import *

SECRET_KEY = 'django-insecure-8(d7#byqkb251$+)0k0kcwwjmt=x7ztx7fqj_a)if$9@j41mbq'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

