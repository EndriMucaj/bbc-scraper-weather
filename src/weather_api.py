import requests
import logging
import os
import spacy
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

nlp = spacy.load("en_core_web_sm")

def extract_location(headline):
    doc = nlp(headline)
    for ent in doc.ents:
        if ent.label_ in ("GPE", "LOC"):
            return ent.text
    return None

def get_weather(location):
    try:
        params = {
            'key': API_KEY,
            'q': location,
            'aqi': 'no'
        }
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        weather = {
            'location': data['location']['name'],
            'country': data['location']['country'],
            'temp_c': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_kph': data['current']['wind_kph']
        }
        logging.info(f"Moti u mor për: {location}")
        return weather

    except requests.exceptions.Timeout:
        logging.error(f"Timeout për vendndodhjen: {location}")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Gabim API për {location}: {e}")
        return None
    except KeyError as e:
        logging.error(f"Të dhëna të pasakta nga API: {e}")
        return None