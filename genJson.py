import json


class Category:
    def __init__(self, category, siteList):
        self.category = category
        self.siteList = siteList

class Site:
    def __init__(self, title, url, description, tags):
        self.title = title
        self.url = url
        self.description = description
        self.tags = tags