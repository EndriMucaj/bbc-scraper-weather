import csv
import json
import logging
import os
from datetime import datetime
from src.scraper import scrape_headlines
from src.weather_api import extract_location, get_weather
from src.security import encrypt_data

OUTPUT_CSV = "data/headlines_weather.csv"
OUTPUT_JSON = "data/headlines_weather.json"

logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_data():
    """Bashkon headlines me të dhënat e motit dhe i ruan."""
    headlines = scrape_headlines()
    results = []

    for headline in headlines:
        location = extract_location(headline)
        weather = get_weather(location) if location else None

        entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'headline': headline,
            'headline_encrypted': encrypt_data(headline),
            'location': location if location else 'N/A',
            'temp_c': weather['temp_c'] if weather else 'N/A',
            'condition': weather['condition'] if weather else 'N/A',
            'humidity': weather['humidity'] if weather else 'N/A',
            'wind_kph': weather['wind_kph'] if weather else 'N/A'
        }
        results.append(entry)
        logging.info(f"U procesua: {headline[:50]}...")

    save_csv(results)
    save_json(results)
    print(f"✅ U procesuan {len(results)} headlines. Të dhënat u ruajtën.")
    return results

def save_csv(data):
    """Ruan të dhënat në CSV."""
    os.makedirs('data', exist_ok=True)
    if not data:
        return
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    logging.info(f"Të dhënat u ruajtën në {OUTPUT_CSV}")

def save_json(data):
    """Ruan të dhënat në JSON."""
    os.makedirs('data', exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.info(f"Të dhënat u ruajtën në {OUTPUT_JSON}")