import environ

from market.cron import *  # noqa

root = environ.Path(__file__) - 3        # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)  # set default values and casting
environ.Env.read_env()                   # reading .env file

SITE_ROOT = root()

USE_L10N = True
USE_i18N = True
USE_TZ = True
TIME_ZONE = env('TIME_ZONE')

# LANGUAGE_CODE = "ru"
FORMAT_MODULE_PATH = [
    'elk.formats'
]

DEBUG = env('DEBUG')    # False if not in os.environ

ALLOWED_HOSTS = [
    'a.elk.today',
    'a-staging.elk.today',
]

SUPPORT_EMAIL = 'help@elk.today'
SERVER_EMAIL = 'django@elk.today'

ADMINS = [
    ('Fedor Borshev', 'f@f213.in'),
]

DATABASES = {
    'default': env.db(),    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

INSTALLED_APPS = [
    'elk',
    'crm',
    'lessons',
    'products',
    'market',
    'timeline',
    'teachers',
    'acc',
    'history',
    'mailer',
    'manual_class_logging',

    'djmoney',
    'anymail',
    'mail_templated',
    'django_countries',
    'django_markdown',
    'django_user_agents',
    'social.apps.django_app.default',
    'easy_timezones',
    'timezone_field',
    'django_nose',
    'django.contrib.admindocs',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'debug_toolbar',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'easy_timezones.middleware.EasyTimezoneMiddleware',
    'elk.middleware.TimezoneMiddleware',
    'elk.middleware.SaveRefMiddleWare',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--nologcapture'
]

ROOT_URLCONF = 'elk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.tz',

                'elk.context_processors.support_email',
                'elk.context_processors.revision',

                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',

            ],
        },
    },
]

SUIT_CONFIG = {
    'ADMIN_NAME': 'ELK Dashboard back-office',
    'MENU_EXCLUDE': ('default',),
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
)
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'acc.pipelines.save_profile_picture',
    'acc.pipelines.save_referral',
    'acc.pipelines.notify_staff',
)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/vendor/jquery/dist/jquery.min.js',
}
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',

    # profiling blocks admin login on the test machine. If you need it — uncomment
    # 'debug_toolbar.panels.profiling.ProfilingPanel',
    #
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

INTERNAL_IPS = [
    '127.0.0.1',
    '::1',
    '77.37.209.221',
    '91.197.114.155',
    '91.197.113.166',
]

SOCIAL_AUTH_URL_NAMESPACE = 'acc:social'

SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, first_name, last_name, email'
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

WSGI_APPLICATION = 'elk.wsgi.application'

public_root = root.path('public/')

MEDIA_URL = env('MEDIA_URL')
MEDIA_ROOT = env('MEDIA_ROOT')

STATIC_URL = env('STATIC_URL')
STATIC_ROOT = env('STATIC_ROOT')

SECRET_KEY = env('SECRET_KEY')  # Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
ANYMAIL = {
    'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('MAILGUN_SENDER_DOMAIN')
}
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_ASYNC = env.bool('EMAIL_ASYNC')
EMAIL_NOTIFICATIONS_FROM = env('EMAIL_NOTIFICATIONS_FROM')

CACHES = {
    'default': env.cache(),
}

BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')

CELERY_TIMEZONE = env('TIME_ZONE')

GEOIP_DATABASE = './geolite/GeoLiteCity.dat'
GEOIPV6_DATABASE = './geolite/GeoLiteCityv6.dat'


# Uncomment this lines to catch all runtime warnings as errors

# import warnings  # noqa
# warnings.filterwarnings(
#     'error', r".*",
#     RuntimeWarning, r".*"
# )
