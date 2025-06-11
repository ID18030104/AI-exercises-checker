
print("=== EXERCISE 1: CARS ===\n")

car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
manufacturers = car_string.split(", ")

print(f"Number of manufacturers: {len(manufacturers)}")

manufacturers_reversed = sorted(manufacturers, reverse=True)
print(f"Manufacturers in reverse order: {manufacturers_reversed}")

manufacturers_with_o = [name for name in manufacturers if 'o' in name.lower()]
print(f"Manufacturers with letter 'o': {len(manufacturers_with_o)} ({manufacturers_with_o})")

manufacturers_without_i = [name for name in manufacturers if 'i' not in name.lower()]
print(f"Manufacturers without letter 'i': {len(manufacturers_without_i)} ({manufacturers_without_i})")

duplicates_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_manufacturers = list(set(duplicates_list))
unique_string = ", ".join(unique_manufacturers)
print(f"\nUnique manufacturers: {unique_string}")
print(f"Number of unique companies: {len(unique_manufacturers)}")

ascending_reversed_letters = [name[::-1] for name in sorted(manufacturers)]
print(f"Ascending order with reversed letters: {ascending_reversed_letters}")

print("\n" + "="*50 + "\n")

print("=== EXERCISE 2: WHAT'S YOUR NAME? ===\n")

def get_full_name(first_name, last_name, middle_name=None):
    """
    Returns a full name with proper capitalization.
    If middle_name is provided, includes it in the full name.
    """
    if middle_name:
        return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"{first_name.title()} {last_name.title()}"

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))
print(get_full_name(first_name="marie", middle_name="elizabeth", last_name="smith"))

print("\n" + "="*50 + "\n")

print("=== EXERCISE 3: FROM ENGLISH TO MORSE ===\n")

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

ENGLISH_DICT = {morse: letter for letter, morse in MORSE_CODE_DICT.items()}

def english_to_morse(text):
    """
    Converts English text to Morse code.
    Letters are separated by spaces, words by slashes.
    """
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_code.append('/')
    
    return ' '.join(morse_code)

def morse_to_english(morse_text):
    """
    Converts Morse code to English text.
    Expects letters separated by spaces and words by slashes.
    """
    words = morse_text.split(' / ')
    english_words = []
    
    for word in words:
        morse_letters = word.split(' ')
        english_letters = []
        
        for morse_letter in morse_letters:
            if morse_letter in ENGLISH_DICT:
                english_letters.append(ENGLISH_DICT[morse_letter])
        
        english_words.append(''.join(english_letters))
    
    return ' '.join(english_words)

print("=== TRADUCTEUR MORSE INTERACTIF ===")
print("Tapez 'quit' pour quitter le programme\n")

while True:
    choice = input("Choisissez une option:\n1. Texte vers Morse\n2. Morse vers Texte\n3. Quitter\nVotre choix (1/2/3): ")
    
    if choice == '1':
        text_input = input("\nEntrez le texte à convertir en Morse: ")
        if text_input.lower() == 'quit':
            break
        morse_result = english_to_morse(text_input)
        print(f"Texte: {text_input}")
        print(f"Morse: {morse_result}\n")
        
    elif choice == '2':
        morse_input = input("\nEntrez le code Morse à convertir (lettres séparées par des espaces, mots par ' / '): ")
        if morse_input.lower() == 'quit':
            break
        english_result = morse_to_english(morse_input)
        print(f"Morse: {morse_input}")
        print(f"Texte: {english_result}\n")
        
    elif choice == '3' or choice.lower() == 'quit':
        print("Au revoir!")
        break
        
    else:
        print("Choix invalide, veuillez choisir 1, 2, ou 3.\n")

print("\n--- Exemples de test automatique ---")
print(f"'SOS' en Morse: {english_to_morse('SOS')}")
print(f"'PYTHON' en Morse: {english_to_morse('PYTHON')}")
print(f"'HELLO WORLD' en Morse: {english_to_morse('HELLO WORLD')}")


test_morse = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(f"Morse '{test_morse}' vers Texte: {morse_to_english(test_morse)}")