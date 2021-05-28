
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seyedmostafa$mo30',
        'USER': 'seyedmostafa',
        'PASSWORD': 'Salam12345',
        'HOST': 'seyedmostafa.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')

STATIC_ROOT=os.path.join(BASE_DIR, 'public/static')
