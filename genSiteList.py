"""
Generates a JSON file from static.html located in /public_html/ directory

Output is also used to generate the text file
python genTextFile.py > wired.txt
"""

import json
from bs4 import BeautifulSoup

class Category:
    def __init__(self, category, subcategories):
        self.category = category
        self.subcategories = subcategories

class SubCategory:
    def __init__(self, title, subcategoryList):
        self.title = title
        self.subcategoryList = subcategoryList

class Site:
    def __init__(self, title, url, description, tags):
        self.title = title
        self.url = url
        self.description = description
        self.tags = tags

source_file = "public_html/index.html"
with open(source_file) as html:
    soup = BeautifulSoup(html, "html.parser")

categories = [] 
for button in soup.find_all("button", {"class": "collapsible"}):
    category = button.text
    categories.append(category)

categoryDivs = []
for content in soup.find_all("div", {"class": "content"}):
    categoryDivs.append(content)

for i, category in enumerate(categories):
    div = categoryDivs[i]
    subCatList = div.find_all('ul')
    print(f"=== {category} ===\n")
    for j, ul in enumerate(subCatList):
        subTitle = ul.find('h3')
        subTitle.extract()
        subTitle = subTitle.text
        if subTitle.endswith(" "):
            subTitle = subTitle[:-1]
        if subTitle.startswith(' '):
            subTitle = subTitle[1:]
        subTitle = subTitle.strip(":")
        print(f"[{subTitle}]\n")
        site_info = subCatList[j].find_all('span')
        for site in site_info:
            if len(site.text) != 0:
                url = site.find('a', href=True)
                title = url.text
                link = url['href']
                url.extract()
                description = site.text
                description = description.replace("-", '')
                description = description.lstrip()
                print(f"{link} - {description}")
        print("\n")