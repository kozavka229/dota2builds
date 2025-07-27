from .base import *

DEBUG = True
ALLOWED_HOSTS += ["127.0.0.1", "localhost"]

STATIC_URL = os.getenv("STATIC_URL", '/static/')
