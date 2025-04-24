# scripts/data_cleaning.py

import pandas as pd
from pathlib import Path

# Define paths
RAW_DATA_PATH = Path("../data/raw/virgin_media_hackathon_raw.xlsx")
OUTPUT_CSV_PATH = Path("../data/processed/cleaned_network_data.csv")


def load_and_clean_data():
    # Load the dataset
    network_df = pd.read_excel(RAW_DATA_PATH, sheet_name='1734454402.5e823cc8223a40924192')

    # Format timestamp
    network_df['timestamp'] = pd.to_datetime(network_df['Date'])
    network_df.drop(columns=['Date'], inplace=True)

    # Drop missing rows
    network_df.dropna(inplace=True)

    # Feature engineering
    network_df['hour'] = network_df['timestamp'].dt.hour
    network_df['weekday'] = network_df['timestamp'].dt.day_name()
    network_df['day'] = network_df['timestamp'].dt.day
    network_df['month'] = network_df['timestamp'].dt.month

    # Save cleaned dataset
    OUTPUT_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    network_df.to_csv(OUTPUT_CSV_PATH, index=False)
    print(f"✅ Cleaned data saved to {OUTPUT_CSV_PATH}")


if __name__ == "__main__":
    load_and_clean_data()
