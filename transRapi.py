
from newsdataapi import NewsDataApiClient
'''
# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_821236fb9af28287b6593378d568428eadbc6")

# You can pass empty or with request parameters {ex. (country = "us")}

response = api.latest_api(language='fr', size=1)

news = response['results'][0]

print(news['title'], " - ", news['description'])
'''
lang='fr'
api = NewsDataApiClient(apikey="pub_821236fb9af28287b6593378d568428eadbc6")
response = api.latest_api(language=lang, size=1)
news = response['results'][0]
print(news)