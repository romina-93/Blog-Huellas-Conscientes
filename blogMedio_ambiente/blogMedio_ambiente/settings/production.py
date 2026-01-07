import os
from .base import *
import dj_database_url

SECRET_KEY = 'django-insecure-8(d7#byqkb251$+)0k0kcwwjmt=x7ztx7fqj_a)if$9@j41mbq'

DEBUG = False

ALLOWED_HOSTS = [
	"blog-huellas-conscientes.onrender.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = None
SESSION_COOKIE_SAMESITE = None


CSRF_TRUSTED_ORIGINS = [
	"https://blog-huellas-conscientes.onrender.com",
]

CSRF_USE_SESSIONS = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}




