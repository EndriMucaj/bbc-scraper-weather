import os
import logging
from src.processor import process_data

# Krijo folderat nëse nuk ekzistojnë
os.makedirs('logs', exist_ok=True)
os.makedirs('data', exist_ok=True)

logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    print("🔍 Duke filluar BBC Headlines Scraper...")
    print("🌍 Duke marrë të dhënat e motit...")
    print("🔐 Duke enkriptuar të dhënat...")
    
    results = process_data()
    
    print(f"\n📊 Rezultatet:")
    print(f"{'HEADLINE':<60} {'VENDI':<15} {'TEMP':<8} {'GJENDJE'}")
    print("-" * 100)
    
    for r in results:
        if r['location'] != 'N/A':
            headline_short = r['headline'][:57] + "..." if len(r['headline']) > 57 else r['headline']
            print(f"{headline_short:<60} {r['location']:<15} {str(r['temp_c'])+'°C':<8} {r['condition']}")
    
    print("\n✅ Të dhënat u ruajtën në data/headlines_weather.csv dhe data/headlines_weather.json")
    print("🔐 Headlines janë enkriptuar në output.")