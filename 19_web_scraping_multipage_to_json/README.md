# 📚 Books To Scrape - Data Scraper

A Python web scraping project that extracts book data (title and price) from [Books to Scrape](https://books.toscrape.com/) and saves it into a JSON file.

---

## 🚀 Features

- Scrapes book data from multiple pages  
- Extracts:
  - 📖 Book Title  
  - 💰 Price  
- Automatically follows pagination (`Next` button)  
- Collects a configurable number of books (default: 70)  
- Saves output in structured JSON format  
- Handles network errors gracefully  

---

## 🛠️ Technologies Used

- Python  
- `requests` – for sending HTTP requests  
- `BeautifulSoup (bs4)` – for parsing HTML  
- `json` – for storing data  
- `urllib.parse` – for handling URLs  

---

## 📦 Installation

1. Clone this repository or copy the script

2. Install required dependencies:

```bash
pip install requests beautifulsoup4
```