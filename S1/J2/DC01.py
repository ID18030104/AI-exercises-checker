while True:
    try:
        word = input("Entrez un mot ou 'quit' pour quitter: ")
        if word.lower() == 'quit':
            print("Merci d'avoir utilisé le programme.")
            break
        if not word.isalpha():
            raise ValueError("Le mot doit contenir uniquement des lettres.")
    except ValueError as e:
        print(e)
        continue

    letter_positions = {}
    for index, letter in enumerate(word):
        letter = str(letter)
        if letter in letter_positions:
            letter_positions[letter].append(index)
        else:
            letter_positions[letter] = [index]
    print(letter_positions)