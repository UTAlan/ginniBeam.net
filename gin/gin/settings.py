"""
Django settings for gin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = '/home/alon10/ginnibeam.net/'
SITE_URL = 'http://www.ginnibeam.net/'
SITE_NAME = 'ginniBeam.net'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ujpb$p)@0yu^oe01zoaeny@5$14zu@42yfsanl#s_ha%zzruv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aboutme',
    'blog',
    'bios',
    'contact',
    'lists',
#    'photos',
    'pics',
    'quotes',
    'users',
    'writings',
    'yoga',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gin.urls'

WSGI_APPLICATION = 'gin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'gin_django',
        'USER': 'alon10',
        'PASSWORD': 'qwer1234',
        'HOST': 'mysql.alanbeam.net',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

MEDIA_ROOT = SITE_ROOT + 'public/media/'
MEDIA_URL = SITE_URL + 'media/'
ADMIN_MEDIA_PREFIX = SITE_URL + 'media/admin/'
STATIC_ROOT = SITE_ROOT + 'gin/static/' 
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    SITE_ROOT + 'public/static/',
)

TEMPLATE_DIRS = (SITE_ROOT + 'gin/templates')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'no-reply@alanbeam.net'
EMAIL_HOST_PASSWORD = 'Aga589!!'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'no-reply@alanbeam.net'
SERVER_EMAIL = 'no-reply@alanbeam.net'

GOOGLE_USER = 'vetamez'
GOOGLE_EMAIL = GOOGLE_USER + '@gmail.com'
GOOGLE_PASS = 'vdaysurprize'

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'

AKISMET_API_KEY = '2c515989c271'

try:
	from local_settings import *
except ImportError:
	pass


