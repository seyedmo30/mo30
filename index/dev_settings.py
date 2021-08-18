import os


from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = []


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
    'debug_toolbar',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mo30',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mo30',
#         'USER': 'hp',
#         'PASSWORD': 'salam',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/')

# STATIC_ROOT = os.path.join(BASE_DIR, 'public/static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'public/static/')
]


