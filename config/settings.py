import os
from pathlib import Path
from celery import Celery
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
# Ensure only your domain can serve the site
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'smallonlinetool.com').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # Added for absolute URL generation
    
    # Third Party Apps
    'tinymce',
    'django_recaptcha',
    
    # Local Apps
    'ads',
    'popups',
    'blog',
    'contact',
    'pages',

    #Tool Apps
    'grass_calc',
    'bark_calc',
    'tons_calc',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ads.context_processors.get_ads',
                'popups.context_processors.popup_data',
                'config.context_processors.latest_posts', 
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASE
# Note: For production, Postgres is highly recommended over SQLite due to concurrency.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATION (Restored for security)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# SITE ID (Required for some contrib apps)
SITE_ID = 1

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES (CSS, JS, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA FILES (User Uploaded Content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT PRIMARY KEY FIELD TYPE
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# RECAPTCHA (Reading from .env)
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')

# If you use valid test keys during dev, keep this. In prod, ensure keys are valid.
# SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

# TINYMCE CONFIGURATION
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': '100%',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen insertdatetime nonbreaking
            directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists charmap print hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen | bold italic underline | fontselect fontsizeselect | forecolor backcolor | 
            alignleft alignright aligncenter alignjustify | bullist numlist outdent indent | 
            removeformat
            ''',
    'menubar': True,
    'statusbar': True,
    'branding': False, 
}

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# CELERY CONFIGURATION
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60 

# Setup Celery App
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# =============================================================================
# PRODUCTION SECURITY SETTINGS
# =============================================================================

# If not in debug mode, enforce HTTPS and secure cookies
if not DEBUG:
    # Redirects all non-HTTPS requests to HTTPS
    SECURE_SSL_REDIRECT = True
    
    # Cookies (Session & CSRF) are only sent over HTTPS
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Proxy SSL Header (Uncomment this if you are behind Nginx, Cloudflare, or AWS ELB)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # HSTS Settings (Tells browser to ONLY use HTTPS for 1 year)
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Other Security Headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# =============================================================================
# GOOGLE SEO & ADS CONFIGURATION
# =============================================================================
# Reading IDs from .env file (or defaults to empty string)
GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID', '')
GOOGLE_SITE_VERIFICATION = os.environ.get('GOOGLE_SITE_VERIFICATION', '')
GOOGLE_ADSENSE_CLIENT_ID = os.environ.get('GOOGLE_ADSENSE_CLIENT_ID', '')
