import csv
import os
from datetime import datetime
import requests

from constants import API_URL, CSV_FILE, PARAMS

def fetch_crypto_data():
    response = requests.get(API_URL, PARAMS)
    return response.json()

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "price"])

        timestamp = datetime.now().strftime("%d-%m-%y %H-%M-%s")
        for coin in data:
            writer.writerow([timestamp, coin['id'], coin['current_price']])
        print("✅ Data saved to csv")