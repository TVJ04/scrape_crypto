django-admin startproject crypto_scraper
cd crypto_scraper
django-admin startapp api

#Install the necessary Python libraries:

pip install djangorestframework celery requests selenium

#Ensure that Redis is running and then start the Celery worker with:
celery -A crypto_scraper worker --loglevel=info

#Run the Django development server:
python manage.py runserver
