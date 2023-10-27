import os
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from django.utils.translation import gettext_lazy
from django.utils.translation import gettext
django.utils.translation.ungettext_lazy=gettext_lazy
django.utils.translation.ugettext_lazy=gettext_lazy
django.utils.translation.ungettext=gettext
from collections.abc import Mapping,Iterator,Sequence
import collections

collections.Mapping=Mapping
collections.Iterator=Iterator
collections.Sequence=Sequence
from django.core.exceptions import FieldDoesNotExist

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '#nv&7=my(8drxahj9-1-_rdmvy8n)$#cdzg0ty1$-aa=unw+$4'

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'rest_framework',
    'chat',
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

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ROOT_URLCONF = 'ChatApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
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

WSGI_APPLICATION = 'ChatApp.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatterboxsql-database',
        'USER': 'chatterboxsql-username',
        'PASSWORD': 'Greaccount3#',
        'HOST': '/cloudsql/chatterboxsql-project:us-west2:chatterboxsql-instance',
        'PORT': '3306',
    }
}
APPEND_SLASH = False

# Password validation

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


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
