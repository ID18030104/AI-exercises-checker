print("Exercise 1:")

def find_largest(numbers):

    return max(numbers)
print(find_largest([1, 2, 3, 4, 5]))
print(find_largest([-10, -5, 0, 5, 10]))
print(find_largest([100, 300, 200, 1000, 500]))

print("\n" + "="*50 + "\n")

print("Exercise 2:")

def check_letter(word, letter):
    if letter in word:
        return f"The letter '{letter}' is in the word '{word}'."
    else: 
        return f"The letter '{letter}' is not in the word '{word}'."
print(check_letter("hello", "e"))
print(check_letter("apple", "z"))
print(check_letter("banana", "a"))

print("\n" + "="*50 + "\n")

print("Exercise 3:")

def count_to_number(n):
    for i in range(1, n + 1):
        print(i)
count_to_number(5)
print("\n")
count_to_number(100)

print("\n" + "="*50 + "\n")




