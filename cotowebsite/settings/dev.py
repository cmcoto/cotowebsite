from .base import *


#HE INCLUIDO AQUI LO DE BASES DE DATOS, porque he puesto en Produccion tambien. Si quiero que quede como antes, debo quitar databases de ambos, y uncomment la original en Base.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        
        #FOR TURSO
      
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#6i3%2)3n-^09&x#!tlxnh-^gdi^z+3$0i@e@3(c$ztb=^qkj3"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*",'127.0.0.1', 'cmcoto.pythonanywhere.com']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
