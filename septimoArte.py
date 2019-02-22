import re
import urllib.request
from pprint import pprint

#p = '/Users/jmanuel/Desktop/Ai/trafico/trafico1.txt'
request = urllib.request.Request(
    "http://infocar.dgt.es/etraffic/Incidencias?ca=13&provIci=28&caracter=acontecimiento&accion_consultar=Consultar&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasOTROS=IncidenciasOTROS&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES&ordenacion=fechahora_ini-DESC")
result = urllib.request.urlopen(request)
pagina = (result.read().decode('utf8'))
#patron1 = '<.*?>'
#patronEspacio = '\s+'
pprint (pagina)

