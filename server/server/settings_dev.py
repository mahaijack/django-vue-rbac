from .settings import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER':'postgres',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':'5432',
    }
}