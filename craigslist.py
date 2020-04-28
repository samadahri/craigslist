from bs4 import BeautifulSoup
import pandas as pd
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive'}

#1 ============================================
print('AtlantaCraigslist')

#input_link = input('Enter the website URL: ')
input_link = 'https://ThomasPerdana.com/recommends/atlantacraigslist/'
links = []
while True:
    res = requests.get(input_link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    links += [i.get('href') for i in soup.findAll('a',{'class':"result-title hdrlnk"})]
    np = soup.find('a',{'class':'button next'}).get('href')
    if len(links) >= 5000:
        links = links[:5000]
        break
    if np != '':
        input_link = 'https://sanantonio.craigslist.org'+np
    else:
        break
    print('.',end='')
print('eop')
results = []
ctr = 1
for link in links:
    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    title = soup.find('h2',{'class':"postingtitle"}).text.strip()
    description = soup.find('section',{'id':"postingbody"}).text.strip()
    results.append((link,title,description))
    if ctr%120 == 0:
        print('.',end='')
    ctr = ctr + 1
print('eop')
df = pd.DataFrame(results,columns=['Link','Title','Description'])
df.to_excel('AtlantaCraigslist.xlsx',index=False)

print('AtlantaCraigslist')
#1 ============================================
