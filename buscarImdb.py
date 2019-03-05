import requests
import re
from bs4 import BeautifulSoup
pattern = "href=\"(.*?)\">"
url = "https://www.imdb.com/find?ref_=nv_sr_fn&q=Alita:+Ángel+de+combate&s=all"
content= requests.get(url)
soup = BeautifulSoup(content.text, "html.parser")
links =[]
#for resultado in soup.findall('tr', attrs={'class':'findResult'},pattern="href=\"(.*?)\">"):
resultado = soup.find('tr', {'class': 'findResult odd'}).find('a').get('href')
#resultado = soup.find('td', {'class':'result_text'})
    print (link)
"""
    for referencia in referencias:
        print (referencia)
        print ("Texto de referencia")
        print (type(referencia))

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)


    for referencia2 in referencia.find(():
        print (referencia2)
"""