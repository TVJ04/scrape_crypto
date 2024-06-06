# api/urls.py

from django.urls import path
from .views import CryptoScrapeView

urlpatterns = [
    path('scrape/', CryptoScrapeView.as_view(), name='crypto-scrape'),
]


#Include the API URLs in the project's main urls.py:
# crypto_scraper/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
