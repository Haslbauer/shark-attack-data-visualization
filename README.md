# Shark Attack Data Visualization

## Overview
This project processes real-world data from the Global Shark Attack File (GSAF), cleans it, enriches it with geographic coordinates, and visualizes it on an interactive world map.

The goal is to transform raw, inconsistent data into a meaningful visual representation that highlights global patterns of shark attacks.

---

## Features
- Data cleaning and preprocessing of real-world datasets
- Geocoding of locations into coordinates
- Interactive world map visualization
- Marker size reflects number of incidents per location
- Color distinction between fatal and non-fatal attacks

---

## Tech Stack
- Python
- pandas (data processing)
- folium (map visualization)
- geopy (geocoding)
- openpyxl (Excel handling)

---

## Project Structure
shark-attack-data-visualization/
├── data/           # raw and processed data files
├── scripts/        # Python scripts for processing and visualization
├── output/         # generated HTML map
├── README.md
├── requirements.txt
└── .gitignore


## How to Run
1. Clone the repository:
```bash
git clone https://github.com/Haslbauer/shark-attack-data-visualization.git
cd shark-attack-data-visualization

2. Install dependencies:
pip install -r requirements.txt

3. Run the data
python scripts/prepare_data.py
python scripts/geocode_locations.py
python scripts/map_shark_attacks.py

4. Open gereated uotput:
output/shark_attack_map.html


## Screenshot of the output on the worldmap
<img width="1118" height="707" alt="image of the generated output" src="https://github.com/user-attachments/assets/cf3b80ed-8343-45af-bfab-ca89ccd6bd69" />
