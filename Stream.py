import streamlit as st
import requests
import os

st.set_page_config(page_title="PSX Data Downloader", layout="wide")
st.title("📉 PSX Historical Data Downloader")

# User input
tickers_input = st.text_input("Enter stock tickers (comma-separated)", "PRL, LOTCHEM, PPL")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

download = st.button("Download CSVs")

if download:
    tickers = [t.strip().upper() for t in tickers_input.split(",")]
    output_dir = "downloaded_psx_data"
    os.makedirs(output_dir, exist_ok=True)

    for symbol in tickers:
        url = f"https://dps.psx.com.pk/historical-download/historical_data.csv?symbol={symbol}&date_from={start_date}&date_to={end_date}"
        response = requests.get(url)
        if response.status_code == 200 and response.content:
            file_path = os.path.join(output_dir, f"{symbol}_data.csv")
            with open(file_path, "wb") as f:
                f.write(response.content)
            st.success(f"✅ Downloaded: {symbol}")
        else:
            st.error(f"❌ Failed to download {symbol}. Check symbol or date.")

    st.info("All downloads complete. Check the downloaded_psx_data folder.")
