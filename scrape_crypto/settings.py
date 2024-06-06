# crypto_scraper/settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
    'django_celery_results',  # for storing Celery results in the database
]

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Assuming Redis is used as a broker
CELERY_RESULT_BACKEND = 'django-db'

# Add Celery to the middleware
MIDDLEWARE = [
    ...
    'django.middleware.security.SecurityMiddleware',
    ...
]

# Rest Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}
