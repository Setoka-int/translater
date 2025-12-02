#program translate
import asyncio
from googletrans import Translator
print("-" * 10, "Переводчик" , "-" * 10)
async def translate_text_async(text_to_translate):
    translator = Translator()

    translate = await translator.translate(text_to_translate, dest='en')

    print(f"Текст на английском: {translate.text}")

text = ""
while True:
    text = input("Введите текст для перевода: ")
    if text.lower() == "стоп":
        print("Окончание перевода")
        break
    asyncio.run(translate_text_async(text))
