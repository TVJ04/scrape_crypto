# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_crypto_data

class CryptoScrapeView(APIView):
    def post(self, request, *args, **kwargs):
        coin_list = request.data.get('coins', [])
        if not coin_list:
            return Response({"error": "No coins provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        task = scrape_crypto_data.delay(coin_list)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
