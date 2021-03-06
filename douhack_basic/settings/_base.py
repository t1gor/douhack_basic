import os
import sys
import datetime
from unipath import Path


from djcelery import setup_loader

# Specific settings
CONFIRM_IN_DAYS = 14

PROJECT_ROOT = Path(__file__).ancestor(3)
sys.path.append(PROJECT_ROOT.child('apps'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Olexandr Shalakhin', 'olexandr@shalakhin.com'),
)

ALLOWED_HOSTS = ['douhack.herokuapp.com']
MANAGERS = ADMINS
TIME_ZONE = 'Europe/Kiev'
LOCALE_PATHS = (PROJECT_ROOT.child('locale'),)
LANGUAGE_CODE = 'ru-UA'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = PROJECT_ROOT.child('media')
MEDIA_URL = '/m/'
STATIC_ROOT = PROJECT_ROOT.child('static_collected')
STATIC_URL = '/s/'
STATICFILES_DIRS = (
    PROJECT_ROOT.child('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = os.environ['SECRET_KEY']

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'douhack_basic.urls'

WSGI_APPLICATION = 'douhack_basic.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_ROOT.child('templates'),
)

PROJECT_APPS = (
    'core',
    'registrations',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'gunicorn',
    'djcelery',
) + PROJECT_APPS

CELERY_TASK_RESULT_EXPIRES = datetime.timedelta(minutes=30)
setup_loader()

ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('ru', ugettext('Russian')),
    ('ua', ugettext('Ukrainian')),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
