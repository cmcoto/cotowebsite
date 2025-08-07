from .base import *

DEBUG = False

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmcoto$default',
        'USER': 'cmcoto',
        'PASSWORD': 'pacesetter',
        'HOST': 'cmcoto.mysql.pythonanywhere-services.com',
    }
}

try:
    from .local import *
except ImportError:
    pass
