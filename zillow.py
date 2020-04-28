from bs4 import BeautifulSoup
import pandas as pd
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive'}



#1 ======================
print('AlabamaZillow')
input_url = 'https://ThomasPerdana.com/recommends/alabamazillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('AlabamaZillow.xlsx',index=False)

print('AlabamaZillow')
#1 ======================



#2 ======================
print('AlaskaZillow')
input_url = 'https://ThomasPerdana.com/recommends/alaskazillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('AlaskaZillow.xlsx',index=False)

print('AlaskaZillow')
#2 ======================





#3 ======================
print('ArizonaZillow')
input_url = 'https://ThomasPerdana.com/recommends/arizonazillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('ArizonaZillow.xlsx',index=False)

print('ArizonaZillow')
#3 ======================







#4 ======================
print('ArkansasZillow')
input_url = 'https://ThomasPerdana.com/recommends/arkansaszillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('ArkansasZillow.xlsx',index=False)

print('ArkansasZillow')
#4 ======================





#5 ======================
print('CaliforniaZillow')
input_url = 'https://ThomasPerdana.com/recommends/californiazillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('CaliforniaZillow.xlsx',index=False)

print('CaliforniaZillow')
#5 ======================




#6 ======================
print('ColoradoZillow')
input_url = 'https://ThomasPerdana.com/recommends/coloradozillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('ColoradoZillow.xlsx',index=False)

print('ColoradoZillow')
#6 ======================




#7 ======================
print('ConnecticutZillow')
input_url = 'https://ThomasPerdana.com/recommends/connecticutzillow/'
results = []
links = []
np=''
np1=''

#input_url = input('Enter the URL: ')

res = requests.get(input_url,headers=headers)

while True:
    if np != '':
        res = requests.get('https://www.zillow.com'+np,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    listings = soup.findAll('a',{'class':"list-card-img"})

    links += [i.get('href') for i in listings]

    np = soup.find('a',{'title':"Next page"}).get('href')
    
    if np == np1:
        break
    np1 = np
    
    print('.',end='')

print('eop')

ctr = 1
for link in links:

    res = requests.get(link,headers=headers)
    soup = BeautifulSoup(res.text,'lxml')

    addressSoup = soup.find('h1',{'class':"ds-address-container"})
    if addressSoup != None:
        address = addressSoup.text
    else:
        address = ''

    description1Soup = soup.find('div',{'class':"ds-summary-row"})
    if description1Soup != None:
        description1 = description1Soup.text
    else:
        description1 = ''

    description2Soup = soup.find('div',{'class':"ds-chip-removable-content"})
    if description2Soup != None:
        description2 = description2Soup.text.strip()
    else:
        description2 = ''

    description3Soup = soup.find('div',{'class':"ds-overview-section"})
    if description3Soup != None:
        description3 = description3Soup.text.strip()
    else:
        description3 = ''
    
    results.append((link,address,description1,description2,description3))

    if ctr%40 == 0:
        print('.',end='')
    ctr = ctr+1

print('eop')

df = pd.DataFrame(results,columns=['Link','Address','Description1','Description2','Description3'])
df.to_excel('ConnecticutZillow.xlsx',index=False)

print('ConnecticutZillow')
#7 ======================