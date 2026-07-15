import os
from dotenv import load_dotenv
from .base import *

# Φόρτωση των environment variables από το .env αρχείο στο root
load_dotenv(os.path.join(BASE_DIR, '.env'))

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Κάνει override την SQLite του base.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'booking_platform'),
        'USER': os.getenv('DB_USER', 'admin'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'admin_password'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}