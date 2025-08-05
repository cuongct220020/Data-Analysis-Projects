import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/jobs/"
page = requests.get(url)
html = BeautifulSoup(page.content, 'html.parser')
print(html)
