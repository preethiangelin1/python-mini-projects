from datetime import datetime
import requests
import sqlite3

from constants import API_URL, DB_NAME, PARAMS

def fetch_crypto_data():
    response = requests.get(API_URL, PARAMS)
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS crypto_prices
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    timestamp TEXt,
                   coin Text,
                   price REAL) 
                   ''')
    conn.commit()
    conn.close()

def save_to_database(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%d-%m-%y %H-%M-%S")
    for coin in data:
        cursor.execute('''
                        INSERT INTO 
                        crypto_prices(timestamp, coin, price) 
                        VALUES(?, ?, ?)
                       ''',
                       (timestamp, coin['id'], coin['current_price']))
        
    conn.commit()
    conn.close()
    print("Price saved to database")
        
def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
                        SELECT timestamp, price FROM crypto_prices
                        WHERE coin = ?
                        ORDER BY timestamp DESC
                        LIMIT 1
                    ''', (coin_name, ))
    result = cursor.fetchone()
    conn.close()
    if result:
        print(f"Price: ${result[1]} - Timestamp: {result[0]}")
    