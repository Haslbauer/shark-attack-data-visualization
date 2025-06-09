🦈 Shark Attack Data Visualization

Projektbeschreibung

Dieses Projekt verarbeitet reale Daten aus der Global Shark Attack File (GSAF), bereinigt sie, reichert sie mit Koordinaten an und stellt sie visuell auf einer Weltkarte dar. Die Vorfälle werden als Marker dargestellt, deren Größe die Anzahl der Angriffe pro Ort widerspiegelt. Farblich wird zwischen tödlichen und nicht-tödlichen Vorfällen unterschieden.

Verwendete Technologien

Python 3.13

pandas – Datenverarbeitung

csv / sqlite3 – Datei- und Datenbankhandling

folium – Kartenvisualisierung

OpenCage API – Geocodierung von Orten

Jupyter / PyCharm – Entwicklungsumgebung

Datenquelle

GSAF5.xls – öffentlich zugänglich unter: https://www.sharkattackfile.net
(enthält Vorfälle seit über 100 Jahren)

Ablauf

Datenauswahl & Filterung
Relevante Spalten extrahieren: Country, Location, Activity, Fatal Y/N, Species, Latitude, Longitude.

Geocodierung (nur wenn notwendig)
Falls Koordinaten fehlen: Ortsangaben werden via OpenCage-API geokodiert (mit Timeout- und Ratenlimit-Schutz).

Karten-Visualisierung
Mit folium wird eine interaktive HTML-Karte erzeugt:

Markergröße = Häufigkeit

Farbe: Rot = ≥ 1 tödlicher Vorfall, Gelb = nur nicht-tödliche

Tooltip mit Art, Aktivität, Ortsname

Projektstruktur

shark_attack_worldwide/
│
├── data/
│   ├── GSAF5.xls
│   ├── gsaf_cleaned.csv
│   └── gsaf_with_coordinates.csv
│
├── scripts/
│   ├── prepare_data.py
│   ├── geocode_locations.py
│   └── map_shark_attacks.py
│
├── .gitignore
├── README.md
└── shark_attack_map.html
Hinweise
Die Geocodierung nutzt einen privaten API-Key (OpenCage). Dieser ist nicht im Repository enthalten und sollte lokal in apikey.txt oder .env gespeichert werden.

Pro Durchlauf werden maximal 500 API-Anfragen verarbeitet. Wiederholtes Ausführen ergänzt schrittweise weitere Einträge.

Ziel & Ausblick
Ziel des Projekts war es, mit realen Daten ein visuelles Analysewerkzeug zu bauen. Der Fokus lag auf dem praktischen Einsatz von APIs, Datenvisualisierung und strukturiertem Datenhandling.
Später denkbar: Clustering, Heatmaps, Zeitverläufe, Ländervergleiche.

