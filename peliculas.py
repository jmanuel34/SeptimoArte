
import requests
import time
import urllib.request
import re
from bs4 import BeautifulSoup
from pprint import pprint


def encuentra_link(titulo):
    request= urllib.request.Request("https://www.imdb.com/find?ref_=nv_sr_fn&q=" +titulo+ "&s=all")
    result = urllib.request.urlopen(request)
    pagina= (result.read().decode('utf8'))
    plink = 'tr class="findResult.*?href="(.*?)".*?</tr>'
    elements = re.findall(plink, pagina, re.DOTALL | re.MULTILINE)
    pprint(elements[0])


URL = "https://www.ecartelera.com/cines/56,0,1.html"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
titulos = soup.select(".lfilmb .lfilmbc h4 span")

for item in titulos:
    print(item.text.replace(" ", "+"))
    rutaItem = (item.text.replace(" ", "+"))
    pprint (rutaItem)
    encuentra_link(rutaItem)
