from .base import *

DEBUG = False

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cmcoto$website',
        'USER': 'cmcoto',
        'PASSWORD': 'pacesetter',
        'HOST': 'cmcoto.mysql.pythonanywhere-services.com',
    }
}

# SECURITY WARNING: keep the secret key used in production secret! YO COPIE Y AGREGUE ESTE... y tambien SECURITY WARNING... QUITARLOS SI NO. 
SECRET_KEY = "django-insecure-#6i3%2)3n-^09&x#!tlxnh-^gdi^z+3$0i@e@3(c$ztb=^qkj3"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*",'127.0.0.1', 'cmcoto.pythonanywhere.com']

try:
    from .local import *
except ImportError:
    pass
