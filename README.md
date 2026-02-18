# BBC Headlines Scraper + Weather API

## Overview
This project scrapes the latest world news headlines from BBC News, automatically detects geographic locations mentioned in each headline using Natural Language Processing (NLP), fetches real-time weather data for those locations via OpenWeatherMap API, and stores the enriched dataset in both CSV and JSON formats. All headlines are encrypted using the Fernet symmetric encryption algorithm before being saved.

---

## Architecture
```
porjektPerfundimtar/
├── src/
│   ├── scraper.py        → Web scraping module (BBC News)
│   ├── weather_api.py    → NLP location extraction + OpenWeatherMap API
│   ├── processor.py      → Data merging, encryption, and storage
│   └── security.py       → Fernet encryption/decryption
├── data/
│   ├── headlines_weather.csv   → Final enriched dataset (CSV)
│   └── headlines_weather.json  → Final enriched dataset (JSON)
├── logs/
│   └── scraper.log       → Runtime logs
├── main.py               → Entry point
├── .env                  → API Key (not uploaded to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Data Flow
```
BBC News (HTML)
      │
      ▼
 scraper.py  ──────────────────────────────────────────────────────┐
 [BeautifulSoup parses h2/h3 tags, extracts unique headlines]      │
      │                                                             │
      ▼                                                             │
 weather_api.py                                                     │
 [spaCy NLP detects GPE/LOC entities from each headline]           │
 [OpenWeatherMap API fetches real-time weather for each location]   │
      │                                                             │
      ▼                                                             │
 security.py                                                        │
 [Fernet encrypts each headline before storage]                     │
      │                                                             │
      ▼                                                             │
 processor.py                                                       │
 [Merges all data into structured records]                          │
      │                                                             │
      ├──► data/headlines_weather.csv                               │
      └──► data/headlines_weather.json                              │
```

---

## Features
- **Dynamic web scraping** — extracts headlines from BBC News World without hardcoded selectors
- **NLP-powered location detection** — uses spaCy `en_core_web_sm` model to detect countries, cities, and regions automatically from headline text (no static country list)
- **Real-time weather enrichment** — fetches temperature, weather condition, humidity, and wind speed for each detected location
- **Symmetric encryption** — all headlines are encrypted using Fernet (AES-128) before being saved
- **Structured logging** — all events, errors, and warnings are logged to `logs/scraper.log`
- **Dual output format** — data is saved in both CSV and JSON

---

## Libraries & Technologies

| Library | Purpose |
|---|---|
| `requests` | HTTP requests for scraping and API calls |
| `beautifulsoup4` | HTML parsing for BBC News |
| `spacy` | NLP-based geographic entity recognition |
| `cryptography` | Fernet symmetric encryption (AES-128) |
| `python-dotenv` | Secure API key management via `.env` |

---

## Encryption Details
This project implements **Fernet symmetric encryption** from the `cryptography` library.

- Algorithm: AES-128-CBC with HMAC-SHA256 for authentication
- A unique encryption key is auto-generated on first run and saved to `secret.key`
- `secret.key` is excluded from GitHub via `.gitignore`
- The field `headline_encrypted` in the output contains the encrypted version of each headline
- Decryption is possible only with the original `secret.key` file

---

## Output Format
Each record in the output contains:

| Field | Description |
|---|---|
| `timestamp` | Date and time of data collection |
| `headline` | Original BBC headline text |
| `headline_encrypted` | Fernet-encrypted version of the headline |
| `location` | Geographic location detected by spaCy |
| `temp_c` | Temperature in Celsius |
| `condition` | Weather condition (e.g. "light rain") |
| `humidity` | Humidity percentage |
| `wind_kph` | Wind speed in km/h |

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/EndriMucaj/bbc-scraper-weather.git
cd bbc-scraper-weather
```

### 2. Install dependencies
```bash
pip install requests beautifulsoup4 cryptography python-dotenv spacy
python -m spacy download en_core_web_sm
```

### 3. Create the `.env` file
Create a file named `.env` in the root folder:
```
WEATHER_API_KEY=your_openweathermap_api_key_here
```
Get a free API key at: https://openweathermap.org/api

### 4. Run the project
```bash
python main.py
```

---

## Output Files
After running, the following files will be generated:
- `data/headlines_weather.csv` — full dataset in CSV format
- `data/headlines_weather.json` — full dataset in JSON format
- `logs/scraper.log` — detailed runtime log
- `secret.key` — encryption key (auto-generated, never share this file)

---

## Security Notes
- The `.env` file containing the API key is excluded from version control via `.gitignore`
- The `secret.key` encryption file is also excluded from GitHub
- No sensitive values are hardcoded anywhere in the source code
- All API keys are loaded exclusively through environment variables