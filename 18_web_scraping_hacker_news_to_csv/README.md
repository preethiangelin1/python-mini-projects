# 📰 Hacker News Top 20 Scraper

A simple Python script that scrapes the **top 20 posts from Hacker News** and saves them into a CSV file.

---

## 🚀 Features

- Fetches latest posts from Hacker News homepage  
- Extracts:
  - Post title  
  - Post URL  
- Saves data into a CSV file (`hn_top20.csv`)  
- Handles network errors gracefully  

---

## 🛠️ Technologies Used

- Python  
- `requests` – for HTTP requests  
- `BeautifulSoup (bs4)` – for HTML parsing  
- `csv` – for writing data  

---

## 📦 Installation

1. Clone this repository or copy the script

2. Install required dependencies:

```bash
pip install requests beautifulsoup4
```

## 🔮 Future Improvements
- Add score, author, and comments count
- Export to JSON format
- Add CLI arguments (e.g., number of posts)
 - Schedule automatic scraping