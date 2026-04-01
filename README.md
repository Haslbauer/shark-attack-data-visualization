# Shark Attack Data Visualization

A Python project for cleaning, enriching, and visualizing real-world shark attack data on an interactive map.

This project was built to work with a real dataset and turn raw data into a clearer, more useful visual representation. The workflow included data cleaning, geocoding, and map-based visualization, with a focus on structuring the project in a practical and understandable way.

## Features
- Load and process real-world shark attack data
- Clean and standardize raw dataset entries
- Enrich location data through geocoding
- Generate an interactive map visualization
- Organize the workflow into separate scripts and folders

## Tech Stack
- Python
- Pandas
- Geopy
- Folium

## What I Learned
- Cleaning and transforming real-world datasets
- Working with missing and inconsistent data
- Using geocoding to enrich location-based information
- Creating interactive map visualizations
- Structuring a Python project with separate scripts and outputs
- Managing dependencies with `requirements.txt`

## Possible Improvements
- Improve data cleaning for edge cases
- Add filters for year, country, or incident type
- Export additional summary statistics
- Improve the user interface and presentation
- Extend the project with a small web frontend
- 
## Screenshot of the output on the worldmap
<img width="1118" height="707" alt="image of the generated output" src="https://github.com/user-attachments/assets/cf3b80ed-8343-45af-bfab-ca89ccd6bd69" />

## How to Run

Make sure Python is installed on your system.

```bash
git clone https://github.com/Haslbauer/shark-attack-data-visualization.git
cd shark-attack-data-visualization
pip install -r requirements.txt
python scripts/prepare_data.py
python scripts/geocode_locations.py
python scripts/map_shark_attacks.py


