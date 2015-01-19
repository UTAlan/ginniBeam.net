# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = '/home/alon10/ginnibeam.net/'
SITE_URL = 'http://www.ginnibeam.net/'
SITE_NAME = 'ginniBeam.net'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['.ginnibeam.net']

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
#    'writings',
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

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'

try:
	from local_settings import *
except ImportError:
	pass


