"""
Checks the status of all links
Outputs active links to active.txt
"""
from bs4 import BeautifulSoup
import requests

static_html = "public_html/static.html" #pull from JSON in future

with open(static_html) as html:
    soup = BeautifulSoup(html, 'html.parser')

active_links = []
for tag in soup.find_all('a', href=True):
    url = tag['href']
    try:
        #add timeout and headers, checks for 404 as opposed to pinging server
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