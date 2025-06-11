print("Exercise 1:")

number=int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = [number * i for i in range(1, length + 1 )]
print(f"The first {length} multiples of {number} are: {multiples}")


print("\n" + "="*50 + "\n")
print("Exercise 2:")

word = input("Enter a word: ")

result = []  

for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result.append(word[i])

cleaned_word = "".join(result)
print("Cleaned word:", cleaned_word)

