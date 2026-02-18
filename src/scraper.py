import requests
from bs4 import BeautifulSoup
import logging
import os

logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

BBC_URL = "https://www.bbc.com/news/world"

def scrape_headlines():
    try:
        logging.info("Duke filluar scraping nga BBC...")
        response = requests.get(BBC_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = []
        tags = soup.find_all('h3')

        for tag in tags:
            text = tag.get_text(strip=True)
            if len(text) > 20:
                headlines.append(text)
                logging.info(f"Headline gjetur: {text}")

        logging.info(f"Gjithsej {len(headlines)} headlines u nxorën.")
        return headlines

    except requests.exceptions.Timeout:
        logging.error("Timeout - BBC nuk u përgjigj.")
        return []
    except requests.exceptions.RequestException as e:
        logging.error(f"Gabim gjatë scraping: {e}")
        return []