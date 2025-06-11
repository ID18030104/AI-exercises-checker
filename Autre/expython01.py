print("Task 1:")
lst1 = [1, 2, 3, 4]
for value in lst1:
    print(value)

print("\n" + "="*50 + "\n")

print("Task 2:")
lst2 = [1, 2, 3, 4]
for value in lst2:
    print(value * 20)

print("\n" + "="*50 + "\n")

print("Task 3:")
names = ["Elie", "Tim ", "Matt"]
premiere_lettre = [name[0] for name in names]
print(premiere_lettre)

print("\n" + "="*50 + "\n")

print("Task 4:")
numbers = [1, 2, 3, 4, 5, 6]
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
even_lst = even_numbers(numbers)
print(even_lst)

print("\n" + "="*50 + "\n")

print("Task 5:")

lst3 = [1, 2, 3, 4, 5]
lst4 = [4, 5, 6, 7, 8]
def common_elements(lst3, lst4):
    return [value for value in lst3 if value in lst4]
common_lst = common_elements(lst3, lst4)
print(common_lst)

print("\n" + "="*50 + "\n")

print("Task 6:")
names = ["Elie", "Tim", "Matt"]
reversed_lowercase = [word.lower()[::-1] for word in names]
print(reversed_lowercase)

print("\n" + "="*50 + "\n")

print("Task 7:")
str1 = "first"
str2 = "third"
common_letters = list(set(str1) & set(str2))
common_letters.sort()
print(common_letters)

print("\n" + "="*50 + "\n")

print("Task 8:")
divisible_par_12 = [num for num in range(1,101) if num % 12 == 0]
print(divisible_par_12)


print("\n" + "="*50 + "\n")

print("Task 9:")

text = "Amazing"
voyelles = "aeiouy AEIOUY"
consonnes = [char for char in text if char not in voyelles]
print(consonnes)

print("\n" + "="*50 + "\n")

print("Task 10:")
task10 = [[0,1,2] for _ in range(3)]
print(task10)

print("\n" + "="*50 + "\n")

print("Task 11:")
task11 = [[i for i in range (10)] for _ in range(10)]
print("[\n  " + ",\n  ".join(str(row) for row in task11) + "\n]")

print("\n" + "="*50 + "\n")
