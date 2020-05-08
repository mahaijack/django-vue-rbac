from .settings import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'you',
        'USER': 'you',
        'PASSWORD': 'you',
        'HOST': 'you',
        'PORT': '5432',
    }
}
