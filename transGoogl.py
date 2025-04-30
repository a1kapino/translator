from googletrans import Translator
import asyncio

joke = 'The shark quickly swam away after sustaining a very serious Chuck Norris bite.'

async def translate_text(arg1):
    async with Translator() as translator:
        result1 = await translator.translate(arg1, dest='uk')
    return result1.text

async def translate_back(arg2):
    async with Translator() as translator:
        result2 = await translator.translate(arg2, src='uk', dest='en')
    return result2.text

ukr1 = asyncio.run(translate_text(joke)) 
print(ukr1)
back1 = asyncio.run(translate_back(ukr1))
print(back1) 