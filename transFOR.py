import requests, json, deepl2

url1 = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url1)
json_data = json.loads(response.text)
joke = json_data['value']
auth_key = "bece38d2-8d63-4944-972c-0f54e85ac750:fx"  
translator = deepl2.Translator(auth_key)

iterations = 2

print(joke)
jokeRe = []
jokeRe.append(joke)

for i in range(iterations):
    trans_ukr = translator.translate_text(jokeRe[i], target_lang="UK").text
    trans_esp = translator.translate_text(trans_ukr, source_lang='UK', target_lang="ES").text
    trans_de = translator.translate_text(trans_esp, source_lang='ES', target_lang="DE").text
    jokeRe.append(translator.translate_text(trans_de, source_lang='DE', target_lang="EN-US").text)

print(jokeRe[iterations])
  
