"""
Generates a textfile from static.html located in /public_html/ directory
Plan to implement better parsing/formatting for the final output.

Usage:
python genTextFile.py > wired.txt
"""
from bs4 import BeautifulSoup

static_html = "public_html/static.html"

with open(static_html) as html:
    soup = BeautifulSoup(html, 'html.parser')

print(soup.get_text())


