import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2(url):
    headers = {
        "User-Agent": "MyWebScraper/1.0 (abc@example.com)"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    headings = []

    for tag in h2_tags:
        headings.append(tag.get_text())

    print(headings)

if __name__ == "__main__":
    get_h2(URL)