import csv
import matplotlib.pyplot as plt
from constants import CSV_FILE

def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['coin'] == coin_id:
                times.append(row['timestamp'])
                prices.append(row['price'])

    if not times:
        print(f"No data found for {coin_id}")

    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()