from crypto import create_table, fetch_crypto_data, save_to_database, search_coin

def main():
    create_table()
    print("1. Fetch and store crypto data")
    print("2. Search latest price for a coin")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        data = fetch_crypto_data()
        save_to_database(data)
    elif choice == "2":
        coin_name = input("Enter coin name: ").strip().lower()
        search_coin(coin_name)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
