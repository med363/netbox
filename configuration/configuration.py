import os
import sys

# PostgreSQL configuration
DATABASE = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv('POSTGRES_DB', 'netbox'),
    'USER': os.getenv('POSTGRES_USER', 'netbox'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'Netbox2024!'),
    'HOST': os.getenv('POSTGRES_HOST', 'postgresql'),
    'PORT': os.getenv('POSTGRES_PORT', '5432'),
    'CONN_MAX_AGE': 300,
}

# Redis configuration
REDIS = {
    'tasks': {
        'HOST': os.getenv('REDIS_HOST', 'redis'),
        'PORT': int(os.getenv('REDIS_PORT', 6379)),
        'DB': int(os.getenv('REDIS_DB_TASKS', 0)),
        'SSL': False,
    },
    'caching': {
        'HOST': os.getenv('REDIS_HOST', 'redis'),
        'PORT': int(os.getenv('REDIS_PORT', 6379)),
        'DB': int(os.getenv('REDIS_DB_CACHING', 1)),
        'SSL': False,
    }
}

# NetBox configuration
SECRET_KEY = os.getenv('NETBOX_SECRET_KEY', 'default-dev-key-change-me')
ALLOWED_HOSTS = os.getenv('NETBOX_ALLOWED_HOSTS', '*').split(',')

# Superuser (sera créé automatiquement via les variables d'environnement)
# Les variables SUPERUSER_NAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD
# sont déjà passées via docker-compose.yml

# Misc settings
LOGIN_REQUIRED = False
PREFER_IPV4 = True
CHANGELOG_RETENTION = 90
RELEASE_CHECK_URL = None
