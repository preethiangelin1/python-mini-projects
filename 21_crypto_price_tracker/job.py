from crypto import fetch_crypto_data, save_to_csv


def job():
    print("Fetching data hourly...")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)