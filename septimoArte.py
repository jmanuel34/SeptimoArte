import requests
import time
from bs4 import BeautifulSoup
URL = "https://www.ecartelera.com/peliculas/indice/o/"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
#results=[]
items = soup.findAll('div',{'class': 'fl-item'})
for item in items:
    item["titulo"] = item.find('p', {'class': 'tit'}).find('a').get_text()
    item["href"] = item.find('a').get('href')
    print(item["titulo"])
    print(item["href"])
    URLdetail=item["href"]
    contentDetail=requests.get(URLdetail)
    soupDetail = BeautifulSoup(content.text,"html.parser")
    itemsDetail= soup.findAll('table', {'class':'datospelicula'})
    for itemDetail in itemsDetail.findAll('tr'):
        detail = {}
        columns=item.findAll('td')
        detail["Anio"]= columns[0].find('td',{'class':'year'}).find('a').get_text()
   #     itemDetail["Anio"] = item.find ('td',{'class':'year'}).find('a').get_text()
        print(detail["Anio"])
 #   time.sleep(3)


#columns[0].find('span', {'class': 'orange'}).get_text()
#get('alt')