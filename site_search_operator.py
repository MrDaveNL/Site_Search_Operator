import pandas as pd
import requests
import time


urls = [
    'nu.nl',
    'ad.nl',
    'besteseospecialist.nl'
    ]

indexes = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

def make_request(url,headers):
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e: 
        raise SystemExit(e)
    return r

for url in urls:
    search_url = f'https://www.google.com/search?q=site%3A{url}&oq=site%3A{url}&aqs=chrome..69i57j69i58.6029j0j1&sourceid=chrome&ie=UTF-8'
    r = make_request(search_url,headers)
    soup = BeautifulSoup(r.text, "html.parser")
    index = soup.find('div',{'id':'result-stats'}).text
    indexes[url] = index 
    time.sleep(1)

df = pd.DataFrame.from_dict(indexes, orient='index', columns=['searchoperator_results'])
df.to_csv('searchoperator_results.csv')
