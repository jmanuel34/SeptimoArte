from requests import get
import requests
from bs4 import BeautifulSoup
#url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
url = "https://www.imdb.com/chart/top?ref_=ft_100"
#response = get(url)
#print(response.text)
content= requests.get(url)
#print (content.text)
soup = BeautifulSoup(content.text, "html.parser")
items = soup.find('tbody')
for item in items.findAll('tr'):
    film = {}
    columns = item.findAll('td')
    film["titulo"] = item.find('td', {'class': 'titleColumn'}).find('a').get_text()

    film["anio"]=item.find('span', {'class':'secondaryInfo'}).get_text()

    film["rating"]=item.find('td',{'class':'ratingColumn imdbRating'}).get_text().replace('\n','')
    print(film)
