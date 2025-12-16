import os
from .base import *

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-temporal"  
)

DEBUG = False

ALLOWED_HOSTS = [
	"blog-huellas-conscientes.onrender.com",
	"localhost",
    "127.0.0.1",
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




