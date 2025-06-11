people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

# Filtrer les noms de 4 lettres ou moins
short_names = filter(lambda name: len(name) <= 4, people)

# Dire bonjour à chacun de ces noms
greetings = map(lambda name: f"Hello {name}!", short_names)

# Affichage
for greeting in greetings:
    print(greeting)