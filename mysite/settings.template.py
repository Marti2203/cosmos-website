"""
#####################################
# TEMPLATE SETTINGS FOR DEVELOPMENT #
#####################################
"""

import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TEXT_ADDITIONAL_TAGS = ('iframe',)
TEXT_ADDITIONAL_ATTRIBUTES = ('scrolling', 'allowfullscreen', 'frameborder', 'src', 'height', 'width')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

raise Exception("SET THIS UP")
X_FRAME_OPTIONS = "SAMEORIGIN"
XS_SHARING_ALLOWED_METHODS = ["POST", "GET", "OPTIONS", "PUT", "DELETE"]
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*1)y(v%aw*_ycj&k2f4zgugs%+w9_(vts9jg!j(-3jy7pjyfrc'
#Requirements from the CMS plugins 
API_VERSION='0.0.0' # FOR FACEBOOK
COSMOS_ID='ANDY'    # FOR The Cosmos Facebook account
TOKEN=''            # ACCESS TOKEN FOR FACEBOOK API
DEFAULT_FROM_EMAIL ='' # Email used to send letters

# Application definition

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'mysite', 'static'),
        )
SITE_ID = 1


TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'mysite', 'templates'),],
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.template.context_processors.media',
                    'django.template.context_processors.csrf',
                    'django.template.context_processors.tz',
                    'sekizai.context_processors.sekizai',
                    'django.template.context_processors.static',
                    'cms.context_processors.cms_settings'
                    ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    #'django.template.loaders.eggs.Loader'
                    ],
                },
            },
        ]


MIDDLEWARE = (
        'cms.middleware.utils.ApphookReloadMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
        'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
        )

INSTALLED_APPS = (
        'djangocms_admin_style',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.redirects',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        'django.utils.translation',
        'letsencrypt',
        'cms',
        'menus',
        'sekizai',
        'treebeard',
        'djangocms_text_ckeditor',
        'easy_thumbnails',
        'djangocms_snippet',
        'mysite',
        'filer',
        #'cmsplugin_filer_file',
        #'cmsplugin_filer_folder',
        #'cmsplugin_filer_image',
        #'cmsplugin_filer_utils',
        'djangocms_googlemap',
        'djangocms_video',
        )

FB_PAGE_ID = '1412994915461745'

LANGUAGES = (
        ## Customize this
        ('en', gettext('en')),
        )

CMS_LANGUAGES = {
        ## Customize this
        1: [
            {
                'redirect_on_fallback': True,
                'hide_untranslated': False,
                'public': True,
                'code': 'en',
                'name': gettext('en'),
                },
            ],
        'default': {
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
            },
        }

CMS_TEMPLATES = (
        ## Customize this
        ('fullwidth.html', 'Fullwidth'),
        )

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

### TODO: ADD CREDENTIALS HERE
DATABASES = {

        # Connection to the remote mysql database
        'default':{

            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',   # Or an IP Address that your DB is hosted on
            'PORT': '',
            }
        }

MIGRATION_MODULES = {

        }
LOGIN_URL ='/login/'
LOGIN_REDIRECT_URL = '/login/'

THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters'
        )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
