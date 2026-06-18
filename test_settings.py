import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'test-secret-key'
DEBUG = True

# Pytest'in ve Django'nun tanıması gereken uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'moderation', # Bizim yazdığımız uygulama
]

# Testler için bellekte çalışıp silinecek geçici veritabanı ayarı
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

USE_TZ = True

ROOT_URLCONF = 'moderation.urls'