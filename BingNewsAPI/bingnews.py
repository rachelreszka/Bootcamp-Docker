

#pip install requests
import requests
import json
url = "https://bing-news-search1.p.rapidapi.com/news/search"

querystring = {"q":"\"Prefeitura de Curitiba\"","sortBy":"Curitiba","setLang":"pt-br","freshness":"Day","textFormat":"Raw","safeSearch":"Off"}

headers = {
	"X-BingApis-SDK": "true",
	"Accept-Language": "pt-br",
	"X-RapidAPI-Key": "4630352aebmsh81f0f3d21aebd92p194e57jsn82bb8c914c62",
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
resposta_json = response.text
dados_json = json.loads(resposta_json)
for site_consulta in enumerate (dados_json['value']):
    print('Titulo:',site_consulta[1]['name'], 
        '\n Link: ',site_consulta[1]['url'], 
        '\n Descrição:',site_consulta[1]['description'], '\n')