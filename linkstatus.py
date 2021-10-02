"""
Checks the status of all links
Outputs active links to active.txt
"""
from bs4 import BeautifulSoup
import requests

static_html = "public_html/static.html"

with open(static_html) as html:
    soup = BeautifulSoup(html, 'html.parser')

active_links = []
for tag in soup.find_all('a', href=True):
    url = tag['href']
    try:
        req = requests.get(url)
        if req.ok:
            print(f"{url}:[LIVE]")
            active_links.append(url)
        else:
            print(f"{url}:[OFFLINE]")
    except Exception:
        pass

with open('active.txt', 'w') as fp:
    for link in active_links:
        fp.write(f"{link}\n")