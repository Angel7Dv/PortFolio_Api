"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
import django_heroku  # HEROKU DEPLOY
import dj_database_url  # HEROKU DEPLOY
import os
from pathlib import Path

import os
import environ  # add this
env = environ.Env(  # add this
    # set casting, default value
    DEBUG=(bool, False)         # add this
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # add this

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # backend
    'corsheaders',
    'rest_framework',
    'ckeditor',

    # apps
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # add this
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 'whitenoise'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# url frontend request
# CORS_ORIGIN_ALLOW_ALL=True
if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:3000',
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        env('CORS_ALLOWED_ORIGINS'),
    ]


ROOT_URLCONF = 'settings.urls'


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.IsAdminUser',
#     ]
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('POSTGRES_NAME'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('POSTGRES_HOST'),
            'PORT': '5432',
        }
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('PRODUCTION_POSTGRES_NAME'),
            'USER': env('PRODUCTION_POSTGRES_USER'),
            'PASSWORD': env('PRODUCTION_POSTGRES_PASSWORD'),
            'HOST': env('PRODUCTION_POSTGRES_HOST'),
            'PORT': '5432',
        }
    }

# # Usa la variable de entorno DATABASE_URL="esta"
# django_heroku.settings(locals())
# options = DATABASES['default'].get('OPTIONS', {})
# options.pop('sslmode', None)
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),

# }


# # SIMPLE_JWT settings https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     # 'ROTATE_REFRESH_TOKENS': True,
#     # 'BLACKLIST_AFTER_ROTATION': True, ## add this for use refresh token and expire access token
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
# }


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/build/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'build', 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'build/static'),
)

MEDIA_URL = '/static/media/'
MEDIA_ROOT = BASE_DIR / 'static/media/'


# X_FRAME_OPTIONS = 'SAMEORIGIN'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
