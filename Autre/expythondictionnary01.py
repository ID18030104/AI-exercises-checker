print("Task 1:")
tuple_list = [("name", "Elie"), ("job", "Instructor")]
result_dictionnaire = dict(tuple_list)
print(result_dictionnaire)

print()

print("Task 2:")
keys = ["CA", "NJ", "RI"]
values = ["California", "New Jersey", "Rhode Island"]
state_dictionnaire = dict(zip(keys, values))
print(state_dictionnaire)

print()

print("Task 3:")

vowels = "aeiou"
vowel_dict = {vowel: 0 for vowel in vowels}
print(vowel_dict)

print()

print("Task 4:")

alphabet_dict = {i: chr(64 + i) for i in range(1, 27)}


for key, value in alphabet_dict.items():
    print(f"{key}: '{value}',")



print()

print("Super Bonus:")
text = "awesome sauce"
vowels = "aeiou"
vowel_count = {vowel: text.lower().count(vowel) for vowel in vowels}
print(vowel_count)
