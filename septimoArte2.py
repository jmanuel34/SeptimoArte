import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.ecartelera.com/cines/56,0,1.html"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
titulos = soup.select(".lfilmb .lfilmbc h4 span")
informacion = soup.select(".lfilmb .lfilmbc p.info")
film ={}
for item in titulos:
#    print(item.text.replace(" ", "+"))
    rutaItem = (item.text.replace(" ", "+"))
    print (rutaItem)
#for item in informacion:
#    print(item)