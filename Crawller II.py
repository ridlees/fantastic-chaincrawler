import requests
from bs4 import BeautifulSoup

def Get_Open_rank(domain):
    import json
    key = 'YOUR_KEY'
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

    return urls
def Start():
    #input
    urls = []
    url = input("URL? \n")
    #needs to be in https://example.com
    print(Href_from_URL(url,urls))
    
if __name__ == "__main__":
    Start()
