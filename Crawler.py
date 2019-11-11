import requests
from bs4 import BeautifulSoup

def Get_Open_rank(domain):
    import json
    key = 'K5MFJyX7+tfsHvDf2yEsA2Ct94st53CrFf7IFghufWI'
    url = 'lol' + domain
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    page = requests.get(url, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    Dictionary=json.loads(str(soup))
    OpenRank = Dictionary.get("data").get(domain).get("openrank")
    print(OpenRank)
    return OpenRank
        
def Href_from_URL(URL,urls):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    page = requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')
    links = soup.findAll("a")
    for link in links:
        url = link.get("href")
        #TODO Check urls if duplicit
        if url in urls != True:
            urls.append(url)
            print("nigga")
        #CSV_format(urls)
    else:
        #CSV_format(urls)
        print("Hellyeah")

def Domain_scrapper(url):
    import re
    domain = re.split('\.',url)[1]
    #TODO test for subdomain :/
    domain_with_fix = domain +"."+re.split('\.',url)[2]
    return domain, domain_with_fix

def Loop_url_fetcher(urls, index,domain):
    for url in urls[int(len(urls) - index), len(urls)]: #Doesn't work
        if domain in url == True:
            urls = Href_from_URL(url, urls)
            #Needs redesign 
            
        '''
        This means makes recursive partial loop which is only for the last index (so first URL, the only Urls 2-X and so on
        that should save time on reruns of the same URLS, cause there will be no duplicit URLS
        then it checks if the requested URL from two-dimensional array contains domain
        TODO add function that scrappes domain from requested URL
'''

def Start():
    #input
    urls = []
    url = input("URL?")
        
    domain, domain_with_fix=Domain_scrapper(url)
    rank = Get_Open_rank(domain_with_fix)
    urls.append([url,rank,"",""])
    Loop_url_fetcher(urls,1,domain)
        
if __name__ == "__main__":
    Start()
