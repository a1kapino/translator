from django.shortcuts import render
from django.http import JsonResponse
from googletrans import Translator
from newsdataapi import NewsDataApiClient
import requests, uuid, json, deepl, asyncio

def choose_news(word, country, lang):
    api = NewsDataApiClient(apikey="pub_821236fb9af28287b6593378d568428eadbc6")
    #new_word = str(translate_text(word, lang))
    response = api.latest_api(q=word, country=country, language=lang, size=1)
    if response['results'] == None:
        news = '  -Not found-  '   
    else: 
        if response['results'][0]['description'] == None:
            news = response['results'][0]['title']+'  --  '
        else:
            news = response['results'][0]['title']+'  --  '+response['results'][0]['description']
    return news
#            newslink = response['results'][0]['link']
#   return news, newslink

async def translate_text(arg, source, dest):
    async with Translator() as translator1:
        result = await translator1.translate(arg, src=source, dest=dest)
    return result.text

def translate_text2(arg, source, dest):
    key = "2gA2orn1yyXoSWkaYPVWykE3VWMLDoJeFddhi7usp8Y3ktvQvCjFJQQJ99BCACPV0roXJ3w3AAAbACOGhkmL"
    constructed_url = "https://api.cognitive.microsofttranslator.com/translate"
    location = "germanywestcentral"
    params1 = {'api-version':'3.0','from': source,'to': dest}
    headers = {'Ocp-Apim-Subscription-Key':key,'Ocp-Apim-Subscription-Region':location,'Content-type':'application/json','X-ClientTraceId':str(uuid.uuid4())}
    body1 = [{'text': arg}]
    request1 = requests.post(constructed_url, params=params1, headers=headers, json=body1)
    response1 = request1.json()
    ukr2 = response1[0]["translations"][0]["text"]
    return ukr2

def translate_text3(arg, source, dest):
    auth_key = "bece38d2-8d63-4944-972c-0f54e85ac750:fx"  
    translator3 = deepl.Translator(auth_key)
    if dest == 'en':
        dest = 'en-GB'
    ukr3 = str(translator3.translate_text(arg, source_lang=source, target_lang=dest))
    return ukr3

def get_joke(request):
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    json_data = json.loads(response.text)
    joke = json_data['value']
    return JsonResponse({ "joke": joke })

def get_news(request):
    word = "Ukraine"
    country = request.GET.get('country', 'ua')   
    lang = request.GET.get('lang', 'uk')
    yournews = choose_news(word, country, lang)
    return JsonResponse({ 'yournews': yournews }, json_dumps_params={'ensure_ascii': False})

def translate(request):
    input = request.GET.get('input', '')
    source = request.GET.get('source', 'en')
    dest = request.GET.get('dest', 'uk')    
    translated = asyncio.run(translate_text(input, source, dest))
    return JsonResponse({ 'translated': translated }, json_dumps_params={'ensure_ascii': False})

def translate2(request):
    input = request.GET.get('input', '')
    source = request.GET.get('source', 'en')
    dest = request.GET.get('dest', 'uk')  
    translated2 = translate_text2(input, source, dest)
    return JsonResponse({ 'translated2': translated2 }, json_dumps_params={'ensure_ascii': False})

def translate3(request):
    input = request.GET.get('input', '')
    source = request.GET.get('source', 'en')
    dest = request.GET.get('dest', 'uk')
    translated3 = translate_text3(input, source, dest)   
    return JsonResponse({ 'translated3': translated3 }, json_dumps_params={'ensure_ascii': False})

def index(request):
    return render(request, 'index.html')
