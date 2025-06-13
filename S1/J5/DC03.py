from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt", ]
translator = Translator()

translations = {}

for word in french_words:
    translated = translator.translate(word, src='fr', dest='en')
    translations[word] = translated.text

print(translations)
