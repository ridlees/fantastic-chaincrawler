# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

class Crawler:

    def rank(self):
        import json
        url = 'https://api.openrank.io/?key=K5MFJyX7+tfsHvDf2yEsA2Ct94st53CrFf7IFghufWI&d=' + self.q
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        page = requests.get(url, headers=headers)
        soup= BeautifulSoup(page.content, 'html.parser')
        Dictionary=json.loads(str(soup))
        rank = Dictionary.get("data").get(self.q).get("openrank")
        if rank == -1:
            self.rank = "No data"
        else:
            self.rank = rank

    def hcsv(self):
        import csv
        try:
            with open(f'{self.domain}_links.csv', 'w', newline='') as csvfile:
                fieldnames = ['link', 'ref', 'title', 'text','external','rank']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for data in self.urls:
                    writer.writerow(self.urls[data])
        except IOError:
            print("I/O error") 

    def robots(self):
        
        page = requests.get(self.https +"/robots.txt")
        robots= BeautifulSoup(page.content, 'html.parser')
        self.robots = robots
        self.sitemap = str(c.robots)[str(c.robots).find("Sitemap:"):]
        
    def Sitemap(self):
        self.sitemap =self.sitemap[self.sitemap.find("https"):]
        page = requests.get(self.sitemap)
        sitemap= BeautifulSoup(page.content, 'html.parser')
        self.sitemap = sitemap
        
    def href(self):
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        page = requests.get(self.http, headers=headers)
        soup= BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("a")
        urls = {}
        
        for link in links:
            
            if link.get("href", 1) != 1:
                
                ref = link.get("ref", "DoFollow")
                title = link.get("title", "no-title")
                text = link.text
                link = link.get("href")
                rank = self.rank
                
                if self.q in link:
                    external = "Internal"
                else:
                    if link[0] == "/":
                        external = "Internal"
                    else:
                        external = "External"
                        l = Crawler(link)
                        l.domain()
                        l.rank()
                        rank = l.rank
                        
                urls.setdefault(link, {'link':link,'ref':ref,'title':title,'text':text,'external':external,'rank':rank})
                
        self.urls = urls
        
        try:
            self.title = soup.findAll("title")[0].text
        except:
            self.title = "None"
        try:
            self.description = soup.findAll("meta", {"name": "description"})[0].get("content")
        except:
            self.description = "None"
        try:
            self.keywords = soup.findAll("meta", {"name": "keywords"})[0].get("content")
        except:
            self.keywords = "None"
            
        self.soup = soup
            
    def domain(self):
        
        import re
        split = re.split('\/',self.url)
        
        if split[0] == "https:":
            self.https = self.url
            self.url = split[2]
            self.http = "http://" + self.url
            
        elif split[0] == "http:":
            self.http = self.url
            self.url = split[2]
            self.https = "https://" + self.url
            
        else:
            self.http ="http://"+self.url
            self.https ="https://"+self.url
            
        domain = re.split('\.',self.url)
        
        if domain[0] == "www":
            self.domain = domain[1]
            self.q =  domain[1]+ "."+ domain[2]
        else:
            self.domain = domain[0]
            self.q =  domain[0]+ "."+ domain[1]
        
    def __init__(self,url):
        self.url = url
        
    
if __name__ == "__main__":
    print("ready")
    c = Crawler("sbazar.cz")
    c.domain()
    c.rank()
    c.href()
    c.hcsv()
    c.robots()
    c.Sitemap()
    print(c.title)
    print(c.description)
    print(c.keywords)
    print(c.robots)
    
