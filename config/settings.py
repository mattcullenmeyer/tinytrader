from pathlib import Path
import os
import datetime
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', False) == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS').split(',')

REST_USE_JWT = True
SIMPLE_JWT = {
  # token expirations must align with frontend
  'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=7), 
  'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=14),
  'LEEWAY': datetime.timedelta(days=1),
}

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites', # need this for allauth

  # Third-party
  'crispy_forms',
  'rest_framework',
  'rest_framework.authtoken', # http://www.tomchristie.com/rest-framework-2-docs/api-guide/authentication#tokenauthentication
  'django_filters', # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
  'allauth', # https://django-allauth.readthedocs.io/en/latest/
  'allauth.account',
  'allauth.socialaccount',
  'corsheaders', # used for making requests from subdomain
  'dj_rest_auth', # used for user authentication endpoints
  'dj_rest_auth.registration', # used for user registration endpoint

  # Local
  'users',
  'pages',
  'blog',
  'api',
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('DATABASE_NAME'),
    'USER': os.getenv('DATABASE_USERNAME'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    'HOST': 'localhost',
    'PORT': '',
  }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# important to include trailing slash / at end of static
STATIC_URL = '/static/'
# STATICFILES_DIRS is location of static files in local development
# this is used to make collectstatic possible so it knows where files live
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 
# STATIC_ROOT is folder where static files will be stored after collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/static')
# STATICFILES_FINDERS tells Django how to look for static file directories
# this is implictly set and therefore optional, but better to make explicit
STATICFILES_FINDERS = [
  "django.contrib.staticfiles.finders.FileSystemFinder",
  "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA_URL is the absolute file to user-uploaded files
MEDIA_URL = '/media/'
# MEDIA_ROOT is the URL we can use in template files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'users.User'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Ensure a tightly secured API by setting default permission class to allow only admins
# https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html
REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
  ),
  'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAdminUser',
  ),
  'DEFAULT_FILTER_BACKENDS': (
    'django_filters.rest_framework.DjangoFilterBackend',
  ),
}

# django-allauth config
LOGIN_REDIRECT_URL = 'pages:home'
ACCOUNT_LOGOUT_REDIRECT = 'pages:home' 
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # use consol instead of smtp until server is configured
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ACCOUNT_SESSION_REMEMBER = True # remember username and password of users
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # only have to enter password once on signup
ACCOUNT_USERNAME_REQUIRED = True 
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email' 
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_UNIQUE_EMAIL = True 
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# Twilio SendGrid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv("SENDGRID_API_KEY")

DEFAULT_FROM_EMAIL = 'matt@tinytrader.io'
