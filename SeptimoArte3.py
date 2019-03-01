import requests
import time
import re
from bs4 import BeautifulSoup
pattern= 'info">(.*?)<span>|</span>(.*?)<span>|</span>(.*?)<span>|</span>(.*?)</p>'
URL = "https://www.ecartelera.com/cines/56,0,1.html"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
items = soup.select(".lfilmbc" )
film = {}

for item in items:
    film["titulo"] = item.find("span").getText()
    ruta = item.find("span").getText()

    film["url"] =  film["titulo"].replace(" ", "+")
    info = str((item.find('p', {"class": "info"})))
    elements = re.findall(pattern, info, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    film["duracion"]= elements[0][0].replace('\n','').replace('\t','')
    film["pais"]= elements[1][1].replace('\n','').replace('\t','')
    film["tipo"]= elements[2][1].replace('\n','').replace('\t','')
    film["clasificacion"]=elements[3][3].replace('\n','').replace('\t','')

    print (film["titulo"])
    print (film["duracion"])
    print(film["pais"])
    print(film["tipo"])
    print (film["clasificacion"])
    print(film["url"])