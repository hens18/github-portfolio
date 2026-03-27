import requests
from bs4 import BeautifulSoup

url = "https://www.flowrestling.org/rankings"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:2000])