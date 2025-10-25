import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Fetch API keys
API_KEY = os.getenv("DATA_API_KEY")

# RAINFALL_RESOURCE_ID = "6c05cd1b-ed59-40c2-bc31-e314f39c6971"
CROP_RESOURCE_ID = "35be999b-0208-4354-b557-f6ca9a5355de"

# Common function to fetch all rows
def fetch_all_data(resource_id):
    all_data = []
    offset = 0
    limit = 10000  # maximum per call

    while True:
        url = f"https://api.data.gov.in/resource/{resource_id}?api-key={API_KEY}&format=json&limit={limit}&offset={offset}"
        response = requests.get(url)
        data = response.json()
        records = data.get("records", [])
        if not records:
            break
        all_data.extend(records)
        offset += limit
        print(f"Fetched {len(all_data)} records so far...")

    return pd.DataFrame(all_data)

# rainfall_df = fetch_all_data(RAINFALL_RESOURCE_ID)
crop_df = fetch_all_data(CROP_RESOURCE_ID)

# rainfall_df.to_csv("rainfall_data.csv", index=False)
crop_df.to_csv("crop_production_data.csv", index=False)

print("✅ Datasets downloaded successfully!")