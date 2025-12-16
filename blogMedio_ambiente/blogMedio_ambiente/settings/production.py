import os
from .base import *

SECRET_KEY = 'django-insecure-8(d7#byqkb251$+)0k0kcwwjmt=x7ztx7fqj_a)if$9@j41mbq'

DEBUG = False

ALLOWED_HOSTS = [
	"blog-huellas-conscientes.onrender.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"


CSRF_TRUSTED_ORIGINS = [
	"https://blog-huellas-conscientes.onrender.com",
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")




