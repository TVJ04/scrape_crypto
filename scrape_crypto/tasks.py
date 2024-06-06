# api/tasks.py

from celery import shared_task
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@shared_task
def scrape_crypto_data(coin_list):
    results = {}
    # Initialize Selenium WebDriver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    for coin in coin_list:
        try:
            url = f'https://www.cryptocompare.com/coins/{coin.lower()}/overview'
            driver.get(url)
            price = driver.find_element(By.CSS_SELECTOR, '.price').text  # Assuming this is the selector for price
            results[coin] = price
        except Exception as e:
            results[coin] = str(e)
    
    driver.quit()
    return results
