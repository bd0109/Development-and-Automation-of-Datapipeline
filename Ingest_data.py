import requests
import pandas as pd
from datetime import datetime

# 1. API endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False
}

# 2. Request the data
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
else:
    raise Exception(f"API request failed with status code {response.status_code}")

# 3. Convert to DataFrame
df = pd.DataFrame(data)

# 4. Save raw data to a file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_json(f"raw_crypto_data_{timestamp}.json", orient='records', indent=2)
print(f"Saved data to raw_crypto_data_{timestamp}.json")

