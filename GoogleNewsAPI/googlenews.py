import json
from GoogleNews import GoogleNews
import datetime
from datetime import timedelta, timezone

GMT = timedelta(hours=-3)
timezoneGMT = timezone(GMT)

date_time = datetime.datetime.now()
date = date_time.astimezone(timezoneGMT)

# Gera as 10 últimas notícias do Google, no período de 1 dia, pesquisando por Prefeitura Municipal de Curitiba
googlenews = GoogleNews(period='3d')
googlenews.setlang('pt')
googlenews.get_news("Prefeitura Municipal de Curitiba")
noticias = googlenews.result()


#for res in noticias:
#  print("Title : ",res["title"])
#  print("News : ",res["desc"])
#  print("Detailed news : ",res["link"])
#  print(noticias)

# Escreve as noticias no arquivo noticias.json
with open('/tmp/noticias.json', 'w', encoding='utf-8') as outfile:  

    for noticia in noticias:    
        if noticia['title'].find("Curitiba") != -1:
            noticia['datetime'] = date.strftime("%Y-%m-%d %H:%M:%S")
            noticia = ({'title': noticia['title'], 'datetime': noticia['datetime'], 'link': noticia['link'], 'site': noticia['site']})
        
            json.dump(noticia, outfile, ensure_ascii=False, indent=3)
            print (noticia)
