import csv
import time
import requests

API_KEY = "cc0d691973e641319b1f42b3065905f6"
input_file = "data/gsaf_clean.csv"
output_file = "data/gsaf_with_coordinates.csv"
MAX_REQUESTS_PER_RUN = 500

# Fortschritt nachverfolgen
processed = set()
try:
    with open(output_file, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            processed.add((row['Country'], row['Location']))
except FileNotFoundError:
    pass

# Dateien öffnen
with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'a', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Latitude', 'Longitude']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    if outfile.tell() == 0:
        writer.writeheader()

    count = 0
    for row in reader:
        key = (row['Country'], row['Location'])
        if key in processed:
            continue

        query = f"{row['Location']}, {row['Country']}"
        url = f"https://api.opencagedata.com/geocode/v1/json?q={query}&key={API_KEY}&limit=1"

        try:
            res = requests.get(url, timeout=5)
            data = res.json()

            if data['results']:
                coords = data['results'][0]['geometry']
                row['Latitude'] = coords['lat']
                row['Longitude'] = coords['lng']
                writer.writerow(row)
                processed.add(key)
                count += 1
                print(f"✔️ {query} → OK")
            else:
                print(f"⚠️ {query} → nicht gefunden")

        except Exception as e:
            print(f"❌ Fehler bei {query}: {e}")
            continue

        time.sleep(1.2)

        if count >= MAX_REQUESTS_PER_RUN:
            print(f"⏹️ {MAX_REQUESTS_PER_RUN} Anfragen erreicht – bitte später fortsetzen.")
            break
