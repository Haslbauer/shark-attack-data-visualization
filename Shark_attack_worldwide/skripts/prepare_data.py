import pandas as pd

# Excel-Datei laden
file_path = "../data/GSAF5.xls"
xls = pd.ExcelFile(file_path)

# Erstes Tabellenblatt
sheet_name = xls.sheet_names[0]
df = pd.read_excel(xls, sheet_name=sheet_name)

# Spaltennamen bereinigen
df.columns = df.columns.str.strip()

# Nur relevante Spalten
columns_needed = ['Country', 'Location', 'Activity', 'Fatal Y/N', 'Species']
df_clean = df[columns_needed].copy()

# NaNs filtern
df_clean.dropna(subset=['Country', 'Location'], inplace=True)

# Species & Fatal standardisieren
df_clean['Species'] = df_clean['Species'].fillna('Unknown').str.strip()
df_clean['Fatal Y/N'] = df_clean['Fatal Y/N'].fillna('N').str.upper().str.strip()

# Exportieren
df_clean.to_csv("gsaf_clean.csv", index=False)
print("✅ Gespeichert als: gsaf_clean.csv")
