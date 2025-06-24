import pandas as pd
import glob
import os

# Step 1: Locate the latest raw data file
list_of_files = glob.glob("raw_crypto_data_*.json")  # Looks for all matching files
if not list_of_files:
    raise FileNotFoundError("No raw_crypto_data_*.json files found in the current directory.")

latest_file = max(list_of_files, key=os.path.getctime)
print(f"Loading latest raw data file: {latest_file}")

# Step 2: Load the most recent raw JSON file
df = pd.read_json(latest_file)

# Step 3: Select necessary columns
df = df[[ 
    'id', 'symbol', 'name', 
    'current_price', 'market_cap', 
    'total_volume', 'last_updated'
]]

# Step 4: Rename columns to match SQL schema
df.rename(columns={
    'id': 'coin_id',
    'symbol': 'coin_symbol',
    'name': 'coin_name',
    'current_price': 'price_usd',
    'market_cap': 'market_cap_usd',
    'total_volume': 'volume_usd',
    'last_updated': 'last_updated_utc'
}, inplace=True)

# Step 5: Format datetime and clean data
df['last_updated_utc'] = pd.to_datetime(df['last_updated_utc'])
df.dropna(inplace=True)

# Step 6: Save to cleaned CSV
df.to_csv("cleaned_crypto_data.csv", index=False)
print("Saved cleaned data to cleaned_crypto_data.csv")

# Optional: Print current working directory for confirmation
print("Working directory:", os.getcwd())
