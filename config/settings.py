"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import json
import os
from datetime import timedelta
from pathlib import Path
from environs import Env
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')
# SECRET_KEY = 'django-insecure-ktjcqow(b9iz%-g6a3gn)7+$7if4f(-()90wx^$^b2a#qv8x%y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = json.loads(os.environ['ALLOWED_HOSTS'])
TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID")
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
HOST = env.str("HOST")

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #  local
    "apps.auth_user",
    "apps.apartment",
    "apps.user",
    'apps.advertising',
    'apps.sendEmail',
    'apps.beautifulSoap',
    'apps.seleniumApp',
    'apps.order',
    'apps.face_recognition',
    'apps.ddos',
    'apps.bot',

    # lib
    'environs',
    'PIL',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework',
    'faker',
    'corsheaders',
    'rest_framework_simplejwt',
    "rest_framework_simplejwt.token_blacklist",
    'django_elasticsearch_dsl',
    'django_elasticsearch_dsl_drf',
    'django_filters',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'config.middlewares.TelegramErrorMiddleware',
    'apps.ddos.middleware.DDOSMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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
AUTH_USER_MODEL = "auth_user.CustomUser"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# DATABASES = {'default': env.dj_db_url('DATABASE_URL')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent

# cd config cat settings.py
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "custom_static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header'
#         },
#         'Basic': {
#             'type': 'basic'
#         }
#     }
# }

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # <-- it is openapi.AutoSchema
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    # "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.MyTokenObtainPairSerializer",
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

CORS_ALLOW_ALL_ORIGINS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "main_format": {
            "format": "{asctime} - {levelname} - {module} - {filename} - {message}",
            "style": "{",
        },
        "console": {
            "format": "{asctime} - {levelname} - {module} - {filename} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "debug.log"),
            "formatter": "main_format",
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 10,
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "INFO",
            "propagate": True,
        },
        # "django.request": {
        #     "handlers": ["file", "console"],
        #     "level": "INFO",
        #     "propagate": True,
        # },
    }

}
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Construction Admin",
    #
    # # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Admin",
    #
    # # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Construction",
    #
    # # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": r'static\logo\logo1.png',

    # # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    # "login_logo": r'logo\logo.png',
    #
    # # Logo to use for login form in dark themes (defaults to login_logo)
    # "login_logo_dark": None,
    #
    # # CSS classes that are applied to the logo above
    # "site_logo_classes": "img-circle",
    #
    # # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    #
    # # Welcome text on the login screen
    "welcome_sign": "Construction Admin panel",
    #
    # # Copyright on the footer
    "copyright": "rustamovdev.uz",
    #
    # # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
    #
    # # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": 'photo',
    #
    # ############
    # # Top Menu #
    # ############
    #
    # # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # {"name": "Дашбоард", "url": "dashboard", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "order"},
        # {"app": "shop"},
    ],
    #
    # #############
    # # User Menu #
    # #############
    #
    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "http:/", "new_window": True},
    #     {"model": "auth.user", "icon": ''}
    # ],
    #
    # #############
    # # Side Menu #
    # #############
    #
    # # Whether to display the side menu
    # "show_sidebar": True,
    #
    # # Whether to aut expand the menu
    # "navigation_expanded": True,
    #
    # # Hide these apps when generating side menu e.g (auth)
    # "hide_apps": ['auth_user'],
    #
    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],
    #
    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["order", "user", "apartment", "advertising", "sendEmail", "selenium"],
    #
    # # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "order": [
            {
                "name": "Телеграм канал ",
                "url": "https://t.me/+rHSr3iwZxV1kYTNiassdf",
                "new_window": True,
                "icon": "fas fa-comments",
            },
            {
                "name": "Телеграм бот",
                "url": "https://t.me/diskont_rassrasdfochkabsdasotasdfasf",
                "new_window": True,
                "icon": "fas fa-robot",
            },
            {
                "name": "Index",
                "url": reverse_lazy("face_recognition"),
                "new_window": True,
                "icon": "fas fa-user",
                "permissions": ["face_recognition.view_index"],
            }

        ]
    },
    # # for the full list of 5.13.0 free icon classes
    "icons": {
        "user.User": "fas fa-user",
        "sendEmail.Email": "fas fa-envelope",  # "fas fa-envelope"
        "apartment.Apartment": "fas fa-building",
        "shop.shop": "fas fa-store",
        "shop.orderGroup": "fas fa-shopping-basket",
        "auth_user.CustomUser": "fas fa-users-cog",
        "auth_user.Manager": "fas fa-user-tie",
        "auth_user.Seller": "fas fa-user",
        "auth_user.BlackListUser": "fas fa-user-slash",
        "auth.Group": "fas fa-users",

    },
    # # Icons that are used when one is not manually specified
    # "default_icon_parents": "fas fa-chevron-circle-right",
    # "default_icon_children": "fas fa-circle",
    #
    # #################
    # # Related Modal #
    # #################
    # # Use modals instead of popups
    # "related_modal_active": False,
    #
    # #############
    # # UI Tweaks #
    # #############
    # # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": None,
    # "custom_js": None,
    # # Whether to show the UI customizer on the sidebar
    # "show_ui_builder": False,
    #
    # ###############
    # # Change view #
    # ###############
    # # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # # - vertical_tabs
    # # - collapsible
    # # - carousel
    # "changeform_format": "horizontal_tabs",
    # # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # # Add a language dropdown into the admin
    # "language_chooser": True,
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

try:
    from .local_settings import *
except ImportError:
    pass
