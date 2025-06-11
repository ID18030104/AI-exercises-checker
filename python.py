books = {
    '1984': 'George Orwell',
    'Brave New World': 'Aldous Huxley',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

print(books['1984'])
books['The Great Gatsby'] = 'Francis Scott Fitzgerald'

books['Moby Dick'] = 'Herman Melville'

print(books.get('To Kill a Mockingbird'))

books.pop('Brave New World')

print(books)

fruits = ("pomme", "poire", "fraise")
print(fruits[0])
fruits = ("pomme", "poire", "fraise", "pomme", "ananas", "ananas", "pomme")
print(fruits.count("fraise"))
print(fruits.index("poire"))

nombres = {3, 1, 4, 5, 9}
nombres.add(6)
print(nombres)
nombres.clear
print(nombres)
nombres_premiers = {2, 3, 5, 7, 11}
print(nombres.intersection(nombres_premiers))
