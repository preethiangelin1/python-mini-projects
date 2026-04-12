# 📊 Crypto Price Tracker

A Python-based project that fetches live cryptocurrency prices, stores them in a CSV file, and visualizes price trends using graphs.

---

## 🚀 Features

- 🔄 Fetches real-time crypto data using CoinGecko API  
- 💾 Stores data with timestamps in a CSV file  
- 📈 Plots price trends for selected cryptocurrencies  
- ⏰ Supports automated hourly data collection  
- 🧾 Displays top cryptocurrencies in the console  

---

## 🛠️ Technologies Used

- Python  
- requests  
- csv  
- matplotlib  
- schedule  

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/preethiangelin1/python-mini-projects.git
cd python-mini-projects/crypto-price-tracker
```

2. Install dependencies:
```bash
pip install requests matplotlib schedule
```

## Usage
```bash
python main.py
```

## Sample Output
```bash
timestamp,coin,price
12-04-26 21-00-01,bitcoin,65000
12-04-26 21-00-01,ethereum,3200
```