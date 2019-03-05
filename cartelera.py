import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint

def obtener_dom(url):
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    return soup

def obtener_valoracion(url):
    soup = obtener_dom(url)
    valoracion = soup.find('div', {'class': 'imdbRating'}).find('span').get_text() if soup.find('div', {'class': 'imdbRating'}) is not None else ""
    return valoracion

def encuentra_link(titulo):
    soup = obtener_dom(dominio + "find?ref_=nv_sr_fn&q=" + titulo + "&s=all")
    url = soup.find('tr', {'class': 'findResult odd'}).find('a').get('href')
    return obtener_valoracion(dominio+url)

pattern= 'info">(.*?)<span>|</span>(.*?)<span>|</span>(.*?)<span>|</span>(.*?)</p>'

dominio = "https://www.imdb.com/"
URL = "https://www.ecartelera.com/cines/56,0,1.html"
soup = obtener_dom(URL)
items = soup.select(".lfilmbc" )
cartelera = []
film = {}

for item in items:
    film["titulo"] = item.find("span").getText()
    print("Obteniendo pelicula " + film['titulo']+ "... ", end="")
    info = str((item.find('p', {"class": "info"})))
    elements = re.findall(pattern, info, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    film["duracion"]= elements[0][0].replace('\n','').replace('\t','')
    film["pais"]= elements[1][1].replace('\n','').replace('\t','')
    film["tipo"]= elements[2][1].replace('\n','').replace('\t','')
    film["clasificacion"]=elements[3][3].replace('\n','').replace('\t','')
    film["valoracion"] = encuentra_link(film["titulo"].replace(" ", "+"))
    print("OK")
    cartelera.append(film)

pprint(cartelera)