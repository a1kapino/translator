import requests, uuid, json

key = "2gA2orn1yyXoSWkaYPVWykE3VWMLDoJeFddhi7usp8Y3ktvQvCjFJQQJ99BCACPV0roXJ3w3AAAbACOGhkmL"
constructed_url = "https://api.cognitive.microsofttranslator.com/translate"
location = "germanywestcentral"

params = {'api-version':'3.0','from':'en','to':'uk'}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

url1 = 'https://api.chucknorris.io/jokes/random'
response1 = requests.get(url1)
json_data = json.loads(response1.text)
joke = json_data['value']

body = [{'text': joke}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

joke1 = response[0]["translations"][0]["text"]
print(joke1)

