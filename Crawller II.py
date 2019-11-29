import requests
from bs4 import BeautifulSoup

def Get_Open_rank(domain):
    import json
    url = 'https://api.openrank.io/?key=K5MFJyX7+tfsHvDf2yEsA2Ct94st53CrFf7IFghufWI&d=' + domain
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    page = requests.get(url, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    Dictionary=json.loads(str(soup))
    OpenRank = Dictionary.get("data").get(domain).get("openrank")
    print(OpenRank)
    return OpenRank
#working rank chacker

def Href_from_URL(URL,urls):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    links = soup.findAll("a")
    for link in links:
        if link.get("href", 1) != 1:
            ref = link.get("ref", "DoFollow")
            title = link.get("title", "notitle")
            text = link.text
            urls.append([link.get("href"),ref,title,text])
            #gets all links from page, gets the ref type, title and text
            #TODO check for duplicity in urls
    return urls

def Robots_for_domain(URL,urls):
    #gets the robots.txt file
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    page = requests.get(URL+"/robots.txt", headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    return soup

def domainconvert(url):
    #example.com
    urlwithhttps = "https://"+url
    urlwithhttp = "http://"+url
    import re
    domain = re.split('\.',url)[0]
    return urlwithhttps,urlwithhttp,domain
    # returns domain for domain check and both addresses (using https and http)

def Start():
    #input
    urls = []
    url = input("URL? \n")
    urlwithhttps,urlwithhttp,domain = domainconvertion(url)
    print(url,urlwithhttps,urlwithhttp,domain)
    #Get_Open_rank(url) -> gets open rank for page
    #print(Href_from_URL(url,urls)) -> gets all urls on page
    #print(Robots_for_domain(url,urls)) -> gets domain for the page
    
if __name__ == "__main__":
    Start()
