"""
Generates a textfile from static.html located in /public_html/ directory

Usage:
python genTextFile.py > wired.txt
"""
from bs4 import BeautifulSoup

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
    print(f"=== {category} ===")
    for j, ul in enumerate(subCatList):
        subTitle = ul.find('h3')
        subTitle.extract()
        subTitle = subTitle.text
        if subTitle.endswith(" "):
            subTitle = subTitle[:-1]
        if subTitle.startswith(' '):
            subTitle = subTitle[1:]
        subTitle = subTitle.strip(":")
        print(subTitle)
        print(subCatList[j].text)

