"""
Django settings for core project.
"""

from pathlib import Path

import environ
from corsheaders.defaults import default_headers
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Security Settings
SECRET_KEY = env.str("SECRET_KEY", default="project-key")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = env("CORS_ALLOW_ALL_ORIGINS", default=True)
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_HEADERS = [*default_headers]

# Environment
ENVIRONMENT_NAME = env.str("ENVIRONMENT_NAME", default="development")
ENVIRONMENT_COLOR = env.str("ENVIRONMENT_COLOR", default="#5AAB61")
ENVIRONMENT_FLOAT = True

# Apps
INSTALLED_APPS = [
    # Django
    'django_admin_env_notice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Packages
    'django_filters',
    'corsheaders',
    'rest_framework',
    # Project
    'apps.finance',
]

# Middleware
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

# Urls
ROOT_URLCONF = 'core.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_admin_env_notice.context_processors.from_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
DATABASES = {"default": env.db("DATABASE_URL")}

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

# Rest Framework Settings
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "base.pagination.AppPagination",
    "PAGE_SIZE": 50,
    # Date Time Formats
    "DATE_FORMAT": "%d/%m/%Y",
    "DATE_INPUT_FORMATS": ["iso-8601", "%d/%m/%Y", "%d-%m-%Y"],
    "EXCEPTION_HANDLER": "base.exceptions.custom_exception_handler",
}

# Internationalization
LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="es-mx")
TIME_ZONE = env.str("TIME_ZONE", default="America/Mexico_City")
USE_I18N = env.bool("USE_I18N", default=True)
USE_L10N = env.bool("USE_L10N", default=True)
USE_TZ = env.bool("USE_TZ", default=True)
LANGUAGES = [
    ("en", _("English")),
    ("es-mx", _("Mexican Spanish")),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = 'static/'
