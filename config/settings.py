from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)n_2l$9@wz_*mvmgw_-^5d2an+l1tx@n*!qvvspu8l44w6kxv5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'debug_toolbar',

    #Aplicaciones de nuestro proyecto
    'ligas',
    'equipos',
    'jugadores',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

<<<<<<< HEAD
import pymysql # type: ignore
=======
import pymysql
>>>>>>> recuperacion
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'futbol',
<<<<<<< HEAD
        'USER': 'alberto',
        'PASSWORD': 'alberto1234',
=======
        'USER': 'root',
        'PASSWORD': 'root1234',
>>>>>>> recuperacion
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

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

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ubicación de los archivos estáticos
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Donde Django almacenará los archivos estáticos en producción

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = ['127.0.0.1',]
<<<<<<< HEAD
=======

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000  # Puedes ajustarlo según lo necesario

LOGIN_URL = "login"  # Página de login a la que se redirige si no está autenticado
LOGIN_REDIRECT_URL = "home"  # Página a la que se redirige tras hacer login
LOGOUT_REDIRECT_URL = "home"  # Página a la que se redirige tras hacer logout
>>>>>>> recuperacion
