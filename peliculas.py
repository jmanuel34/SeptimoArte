import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint


def encuentra_link(titulo):
    request= requests.get("https://www.imdb.com/find?ref_=nv_sr_fn&q=" +titulo+ "&s=all")
    req= request.text
    plink = '<tr class="findResult odd"> <td class="primary_photo"> <a href="(.*?)".*?</tr>'
#    plink = '.?*(/title/.*?">'
    elements = re.search(plink, req, re.DOTALL | re.MULTILINE)
    print(elements(0))
    print(elements)

#<td class="result_text"> <a href="/title/tt0437086/?ref_=fn_al_tt_1" >

URL = "https://www.ecartelera.com/cines/56,0,1.html"
content = requests.get(URL)
soup = BeautifulSoup(content.text, "html.parser")
titulos = soup.select(".lfilmb .lfilmbc h4 span")

for item in titulos:
    print(item.text.replace(" ", "+"))
    rutaItem = (item.text.replace(" ", "+"))
    encuentra_link(rutaItem)
