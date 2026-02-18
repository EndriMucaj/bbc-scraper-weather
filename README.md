# BBC Headlines Scraper + Weather API

## Përshkrimi
Ky projekt nxjerr headlines nga BBC News World, identifikon vendet e përmendura,
merr të dhënat e motit për ato vende përmes WeatherAPI, dhe i ruan të dhënat
e bashkuara në CSV dhe JSON. Headlines enkriptohen me algoritmin Fernet (AES-128).

## Arkitektura e Zgjidhjes
```
porjektPerfundimtar/
├── src/
│   ├── scraper.py       → Web scraping nga BBC News
│   ├── weather_api.py   → Integrimi i WeatherAPI
│   ├── processor.py     → Bashkimi dhe ruajtja e të dhënave
│   └── security.py      → Enkriptimi Fernet (AES-128)
├── data/                → Output CSV dhe JSON
├── logs/                → Log skedarët
├── main.py              → Pika hyrëse
├── .env                 → API Key (nuk ngarkohet në GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

## Rrjedha e të Dhënave
1. `scraper.py` → nxjerr headlines nga BBC News World
2. `weather_api.py` → identifikon vendet dhe merr motin
3. `security.py` → enkripton headlines me Fernet
4. `processor.py` → bashkon gjithçka dhe ruan në CSV/JSON

## Libraritë e Përdorura
- `requests` — HTTP requests për scraping dhe API
- `beautifulsoup4` — parsing i HTML
- `cryptography` — enkriptim Fernet (AES-128)
- `python-dotenv` — menaxhim i sigurt i API keys

## Enkriptimi
Projekti përdor enkriptim simetrik **Fernet** nga libraria `cryptography`.
Çelësi gjenerohet automatikisht dhe ruhet në `secret.key` (nuk ngarkohet në GitHub).
Fusha `headline_encrypted` në output përmban headline-in e enkriptuar.

## Udhëzime për Ekzekutim

### 1. Instalo libraritë
```bash
pip install requests beautifulsoup4 cryptography python-dotenv
```

### 2. Krijo skedarin .env
```
WEATHER_API_KEY=çelësi_yt_këtu
```

### 3. Ekzekuto projektin
```bash
python main.py
```

### 4. Rezultatet
- `data/headlines_weather.csv` — të dhënat e plota
- `data/headlines_weather.json` — format JSON
- `logs/scraper.log` — log i ekzekutimit