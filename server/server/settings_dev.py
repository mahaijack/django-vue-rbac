from .settings import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cnas',
        'USER':'ctcuser',
        'PASSWORD':'ctcuser',
        'HOST':'121.36.23.77',
        'PORT':'5432',
    }
}