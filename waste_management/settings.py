"""
Django settings for waste_management project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
REDIS_URL = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379')
DATABASE_URL = os.environ.get('DATABASE_URL')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!vqtv4vivkw$!^^33nf+mv(mcu2na0vo3t2jrglm163mdqdyj&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True




# Allow all subdomains of Render and local development
ALLOWED_HOSTS = [
    'waste-management-mfuy.onrender.com',  # Your exact Render domain
    '.onrender.com',                       # Allow ALL Render domains (flexibility)
    'localhost',
    '127.0.0.1',
]
CSRF_TRUSTED_ORIGINS = ['https://waste-management-mfuy.onrender.com']
# Optional: Dynamically allow Render's internal host (if needed)
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    

ASGI_APPLICATION = 'waste_management.asgi.application'


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'users',
    'waste',
    'matching',
    'analytics',
    'education',
    'educ',
    'report',
    'widget_tweaks',
    "channels",
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 Add this
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'waste_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.quick_access_status',
                'django.template.context_processors.debug',
            ],
        },
    },
]

WSGI_APPLICATION = 'waste_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if DATABASE_URL:
    # Production (Render)
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # Local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'new_db',
            'USER': 'postgres',
            'PASSWORD': 'Rach03$%',  # Secure this in a .env file for local dev
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': '<your_cloud_name>',
    'API_KEY': '<your_api_key>',
    'API_SECRET': '<your_api_secret>',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# settings.py

# Static files (CSS, JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # This is where your static files live in development
STATIC_ROOT = BASE_DIR / 'staticfiles'    # This is where they get collected for production

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



TIME_ZONE = 'Africa/Nairobi'  # EAT is UTC+3, and Africa/Nairobi corresponds to this timezone
USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# In waste_management/settings.py
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'  # Default redirect after login (can change to 'matching:matching' later)
LOGOUT_REDIRECT_URL = '/users/login/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py
# settings.py
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [{
                "address": "rediss://default:AXIrAAIjcDE2ZGY1YTlmNTYxMTU0YWM0OWM1MTVlYTM4YTI0YjQwM3AxMA@valid-oarfish-29227.upstash.io:6379",
                "ssl_cert_reqs": None  # Disables SSL verification
            }],
        },
    },
}
