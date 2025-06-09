import csv
import time
import os
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent="shark-geo")
input_file = "../data/gsaf_clean.csv"
output_file = "../data/gsaf_with_coordinates.csv"
batch_size = 50

# 1. Vorhandene Einträge laden
processed_locations = set()
if os.path.exists(output_file):
    with open(output_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row['Country'], row['Location'])
            processed_locations.add(key)

# 2. Neue Einträge vorbereiten
entries_to_process = []
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (row['Country'], row['Location'])
        if key not in processed_locations:
            entries_to_process.append(row)

print(f"🔎 Noch zu verarbeiten: {len(entries_to_process)} Orte")

# 3. Geocoding für bis zu 50 Einträge
results = []
count = 0

def get_coordinates(location_string):
    try:
        loc = geolocator.geocode(location_string)
        if loc:
            return loc.latitude, loc.longitude
    except GeocoderTimedOut:
        return get_coordinates(location_string)
    return None, None

for row in entries_to_process:
    if count >= batch_size:
        break
    loc_string = f"{row['Location']}, {row['Country']}"
    lat, lon = get_coordinates(loc_string)
    print(f"{loc_string} → {lat}, {lon}")
    row['Latitude'] = lat
    row['Longitude'] = lon
    results.append(row)
    time.sleep(1.5)  # wichtig!
    count += 1

# 4. In Datei speichern (anhängen oder neu)
file_exists = os.path.exists(output_file)
with open(output_file, mode='a' if file_exists else 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
    if not file_exists:
        writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"✅ {len(results)} neue Einträge gespeichert → {output_file}")
