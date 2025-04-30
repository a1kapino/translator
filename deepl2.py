import requests, uuid, json, deepl, asyncio
from django.http import JsonResponse

auth_key = "bece38d2-8d63-4944-972c-0f54e85ac750:fx"  # Replace with your key

def translate_text3(arg, dest):
    auth_key = "bece38d2-8d63-4944-972c-0f54e85ac750:fx"  
    translator3 = deepl.Translator(auth_key)
    ukr3 = translator3.translate_text(arg, target_lang=dest)
    return ukr3

arg1='hello all'
dest1='UK'

a1=translate_text3(arg1, dest1)
print(type(str(a1)))

def translate_text2(arg, dest):
    key = "2gA2orn1yyXoSWkaYPVWykE3VWMLDoJeFddhi7usp8Y3ktvQvCjFJQQJ99BCACPV0roXJ3w3AAAbACOGhkmL"
    constructed_url = "https://api.cognitive.microsofttranslator.com/translate"
    location = "germanywestcentral"
    params1 = {'api-version':'3.0','from':'en','to': dest}
    headers = {'Ocp-Apim-Subscription-Key':key,'Ocp-Apim-Subscription-Region':location,'Content-type':'application/json','X-ClientTraceId':str(uuid.uuid4())}
    body1 = [{'text': arg}]
    request1 = requests.post(constructed_url, params=params1, headers=headers, json=body1)
    response1 = request1.json()
    ukr2 = response1[0]["translations"][0]["text"]
    return ukr2

a2=translate_text2(arg1, dest1)
print(type(a2))

