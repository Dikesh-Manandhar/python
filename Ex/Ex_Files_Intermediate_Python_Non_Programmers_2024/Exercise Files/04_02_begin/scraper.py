import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
response = requests.get(url, headers={"User-Agent": "Dikesh"})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")


map_data = list(map(lambda a_tag: a_tag.get_text(), a_tags))
print(map_data)