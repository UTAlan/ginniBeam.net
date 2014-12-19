import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = '/Users/abeam/htdocs/ginnibeam.net/'
SITE_URL = 'http://localhost'

DEBUG = True

MEDIA_ROOT = SITE_ROOT + 'public/media/'
MEDIA_URL = SITE_URL + 'media/'
ADMIN_MEDIA_PREFIX = SITE_URL + 'media/admin/'
STATIC_ROOT = SITE_ROOT + 'gin/static/' 
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    SITE_ROOT + 'public/static/',
)

TEMPLATE_DIRS = (SITE_ROOT + 'gin/templates')


