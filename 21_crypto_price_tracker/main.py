from crypto import fetch_crypto_data, save_to_csv
from graph import plot_graph

def main():
    print("Fetching live crypto data....")
    crypto_data = fetch_crypto_data()
    save_to_csv(crypto_data)

    print("-" * 30)
    for coin in crypto_data:
        print(f"{coin['id']} - ${coin['current_price']}")
    print("-" * 30)

    choice = input("Enter the coin name to get graph: ").strip().lower()

    if choice:
        plot_graph(choice)

if __name__ == "__main__":
    main()