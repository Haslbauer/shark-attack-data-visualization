import csv
import folium
from collections import defaultdict

# 🌍 Karte vorbereiten
shark_map = folium.Map(location=[0, 0], zoom_start=2)

# 📂 CSV-Datei einlesen
input_file = "../data/gsaf_with_coordinates.csv"
locations = defaultdict(list)

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            lat = float(row['Latitude'])
            lon = float(row['Longitude'])
            key = (lat, lon)
            locations[key].append(row)
        except:
            continue  # Zeile überspringen, falls ungültige Koordinaten

# 📍 Marker hinzufügen
for (lat, lon), incidents in locations.items():
    count = len(incidents)
    fatal_count = sum(1 for i in incidents if i['Fatal Y/N'] == 'Y')
    activity = incidents[0].get('Activity', 'Unbekannt')
    species = incidents[0].get('Species', 'Unbekannt')
    location_name = incidents[0].get('Location', 'Unbekannt')

    # 🔴 Farbe: Rot = tödlich, Gelb = nicht tödlich
    color = "red" if fatal_count > 0 else "yellow"

    tooltip = f"{location_name} ({count} Vorfälle)\nArt: {species}\nAktivität: {activity}"

    folium.CircleMarker(
        location=[lat, lon],
        radius=3 + count * 0.5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=tooltip
    ).add_to(shark_map)

# 💾 Karte speichern
shark_map.save("shark_attack_map.html")
print("🗺️ Karte gespeichert als: shark_attack_map.html")
