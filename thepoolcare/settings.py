import os
from pathlib import Path
from django.contrib.messages import constants as messages


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-s-9kak=wb&%6e91qx_b7a8-z2l6da4^8-g=f1(07le0#w_e$&1'

DEBUG = False

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "whitenoise.runserver_nostatic",
    'rj_auth',
    'contact',
    # '',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", # added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thepoolcare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "contact.context_api.show_us"
            ],
        },
    },
]

WSGI_APPLICATION = 'thepoolcare.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'extra/staticfiles')
# STATIC_ROOT = "/home/myusername/webapp/static"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'extra/static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'extra/media')
MEDIA_URL = '/media/'

# Django messages
MESSAGE_TAGS = {
    messages.DEBUG : 'alert-info',
    messages.INFO : 'alert-info',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
    messages.ERROR : 'alert-danger',
}

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'rj_auth.Account'