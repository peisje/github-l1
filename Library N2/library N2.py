from bs4 import BeautifulSoup
import requests

#esimene Ülesanne
url = "https://news.ycombinator.com"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all("a", class_="storylink")
if not titles:
    titles = soup.find_all("span", class_="titleline")
    
for i in range(10):
    print(f"{i + 1}. {titles[i].text}")

