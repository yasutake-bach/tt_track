from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rnt@$_j)02_f0#=q#%p_5q02h59orb1z0w*wbm3&tj497-4_x3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#ロギング設定
LOGGING = {
    'version': 1, # 1固定
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers': {
        #Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level':'INFO',
        },
        #trackアプリケーションが利用するロガー
        'track': {
            'handlers': ['console'],
            'level':'DEBUG',
        },
    },

    #ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    #フォーマッタの設定
    'formatters': {
        'dev': {
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ]),
        },
    },
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
