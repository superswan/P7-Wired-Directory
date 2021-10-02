"""
Generates a JSON file from static.html located in /public_html/ directory

Output is also used to generate the text file. This script can be deprecated
once the JSON file is populated.

For text file:
python genTextFile.py > wired.txt
"""
import jsonpickle
from bs4 import BeautifulSoup

class Category:
    def __init__(self, category, subcategories):
        self.category = category
        self.subcategories = subcategories

class SubCategory:
    def __init__(self, title, subcategoryList):
        self.title = title
        self.sites = subcategoryList

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

categoryObjs = []

# Makes a list of objects to be dumped into JSON
for i, category in enumerate(categories): # Main section categories
    div = categoryDivs[i]
    subCatList = div.find_all('ul')
    print(f"=== {category} ===\n")

    subCatObjs = []
    for j, ul in enumerate(subCatList): # Get subcategories and associated sites
        subTitle = ul.find('h3')
        subTitle.extract()
        subTitle = subTitle.text
        subTitle = subTitle.rstrip().lstrip()
        subTitle = subTitle.strip(":")
        print(f"[{subTitle}]\n")
        site_info = subCatList[j].find_all('span') #Subcategory ul element

        siteObjs = []
        for site in site_info:
            if len(site.text) != 0:
                url = site.find('a', href=True)
                title = url.text
                link = url['href']
                url.extract()
                description = site.text
                description = description.replace("-", '')
                description = description.lstrip()
                print(f"{title}:{link} - {description}")
                tags = []
                site = Site(title, link, description, tags)
                siteObjs.append(site)
        subcat = SubCategory(subTitle, siteObjs)
        subCatObjs.append(subcat)
        print("\n")
    categoryObj=Category(category, subCatObjs)
    categoryObjs.append(categoryObj)

json_data = jsonpickle.encode(categoryObjs, unpicklable=False)
with open('site-list.json', 'w') as outputf:
    print(json_data, file=outputf)