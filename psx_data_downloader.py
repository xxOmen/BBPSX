
import os
import requests
import pandas as pd
from datetime import datetime

# === CONFIGURATION ===
tickers = ["PRL", "LOTCHEM", "PPL", "ENGRO", "SYS"]
start_date = "2025-04-01"
end_date = "2025-05-17"
output_dir = "psx_data"

# === FUNCTION ===
def download_psx_data(symbol, start, end, folder):
    url = f"https://dps.psx.com.pk/historical-download/historical_data.csv?symbol={symbol}&date_from={start}&date_to={end}"
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(folder, f"{symbol}_data.csv")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {symbol}")
    else:
        print(f"Failed to download {symbol}: Status code {response.status_code}")

# === MAIN ===
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for ticker in tickers:
    download_psx_data(ticker, start_date, end_date, output_dir)

print("Download complete.")
