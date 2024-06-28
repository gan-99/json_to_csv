import pandas as pd
import json

# Path to the JSON file
json_file_path = 'rawInput000 (3).json'

# Load JSON data
with open(json_file_path) as f:
    data = json.load(f)

# Normalize JSON data
df = pd.json_normalize(data)

# Path to the output CSV file
csv_file_path = 'output.csv'

# Save to CSV
df.to_csv(csv_file_path, index=False)

print("Data has been successfully converted to CSV and saved as 'output.csv'")
