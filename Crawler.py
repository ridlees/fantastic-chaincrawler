import requests
from bs4 import BeautifulSoup
        
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
            
        CSV_format(urls)
    else:
        CSV_format(urls)


def Domain_scrapper(url):
    import re
    domain = re.split('\.',url)[1]
    #TODO test for subdomain :/
    return domain

def Loop_url_fetcher(urls, index,domain):
    for url in urls(len(urls) - index, len(urls)):
        if domain in url == True:
            urls = Href_from_URL(URL, urls)
            #Needs redesign 
            
        '''
        This means makes recursive partial loop which is only for the last index (so first URL, the only Urls 2-X and so on
        that should save time on reruns of the same URLS, cause there will be no duplicit URLS
        then it checks if the requested URL from two-dimensional array contains domain
        TODO add function that scrappes domain from requested URL
'''

def Start():
    #input
    urls[]
    url = input("URL?")
    #TODO domain rank checker and other fluffy things
    urls.append([url,rank,"",""])
    domain=Domain_srapper(url)
    Loop_url_fetcher(urls,1,domain)
        
if __name__ == "__main__":
    Start()
