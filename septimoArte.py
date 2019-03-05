#############################
# Usar solo para comentarios
#############################
"""
import requests
import time
from bs4 import BeautifulSoup
URL = "https://www.ecartelera.com/cines/56,0,1.html"
#URL = "https://www.ecartelera.com/peliculas/indice/m/"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
#results=[]
items = soup.findAll('div',{'class': 'fl-item'})
for item in items:
#item["titulo"] = item.find('span', {'class': 'tit'}).find('a').get_text()
    item["titulo"] = item.find('span').get('href')
    item["href"] = item.find('a').get('href')
    print(item["titulo"])
    print(item["href"])
    URLdetail=item["href"]
    contentDetail=requests.get(URLdetail)
    soupDetail = BeautifulSoup(content.text,"html.parser")
    itemsDetail= soupDetail.findAll('tbody')
    print(soupDetail.prettify())

    for itemDetail in itemsDetail.findAll('tr'):
        detail = {}
        columns=item.findAll('td')
        print(soup.prettify())
        
        print (columns[0].find('span',{'class':'year' }))
          detail["Anio"]= columns[0].find('td',{'class':'year'})
   #     itemDetail["Anio".] = item.find ('td',{'class':'year'}).find('a').get_text()
       
 #   time.sleep(3)


#columns[0].find('span', {'class': 'orange'}).get_text()
#get('alt')
"""
