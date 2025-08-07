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

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*",'127.0.0.1', 'cmcoto.pythonanywhere.com']

try:
    from .local import *
except ImportError:
    pass
