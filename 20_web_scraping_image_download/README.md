# 📚 Book Cover Image Downloader

A Python web scraping project that downloads **book cover images** from [Books to Scrape](https://books.toscrape.com/) and saves them locally.

---

## 🚀 Features

- Scrapes book cover images from the homepage  
- Downloads **top 10 book images**  
- Automatically creates an `images/` directory  
- Cleans filenames to make them safe for storage  
- Handles download errors gracefully  
- Saves images with meaningful filenames  

---

## 🛠️ Technologies Used

- Python  
- `requests` – for HTTP requests and image downloading  
- `BeautifulSoup (bs4)` – for parsing HTML  
- `os` – for file and directory handling  
- `re` – for filename sanitization  
- `urllib.parse` – for building absolute URLs  

---

## 📦 Installation

1. Clone this repository or copy the script

2. Install required dependencies:

```bash
pip install requests beautifulsoup4
```