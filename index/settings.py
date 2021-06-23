

deploy = True

import os


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

INSTALLED_APPS = [
    'general',
    'profiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django.contrib.sitemaps',   
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'public/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

ROOT_URLCONF = 'index.urls'

WSGI_APPLICATION = 'index.wsgi.application'

SECRET_KEY = 'yk$&_3ia7g07rvu79_-r^8=-m82sm3gi_j_%t5tv)-qv&4zb@_'

AUTH_USER_MODEL = 'profiles.CustomUser'

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'


MEDIA_URL = '/media/'


if deploy:
    from .dep_settings import *
else:
    from .dev_settings import *

