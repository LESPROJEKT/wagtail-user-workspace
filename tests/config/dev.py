from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PSSWD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": 5432,
    }
}

DEBUG=True

SECRET_KEY="super-secret"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]

USER_WORKSPACE_PAGE_MODEL = "tests.ValidWorkspacePage"


