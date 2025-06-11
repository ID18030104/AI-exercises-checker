def repeat_word(word, number):
    """
    Prints a word the specified number of times.
    
    Args:
        word (str): The word to repeat
        number (int): How many times to print the word
    """
    for i in range(number):
        print(word)

# Example usage:
repeat_word("hello", 3)
print()  # Empty line for separation
repeat_word("goodbye", 2)

a = ["b", "g", "a", "d", "f", "c", "h", "e"]
x = sorted(a)
print("a after sorted function")
print(a)
print(x)
b = [1, 2, 5, 8, 3]
b.sort()
print(b)

word = input("Entrez un mot: ")

# Créer le dictionnaire des positions
letter_positions = {}

# Parcourir chaque lettre avec son index
for index, letter in enumerate(word):
    letter = str(letter)  # S'assurer que c'est une string
    
    if letter in letter_positions:
        letter_positions[letter].append(index)
    else:
        letter_positions[letter] = [index]

# Afficher le résultat
print(letter_positions)