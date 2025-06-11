print("Exercise 1:")

def add_two_numbers (a, b):
    return a + b

print (add_two_numbers(2, 5))

print("\n" + "="*50 + "\n")

print("Exercise 2:")

def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
print(greet("Bob"))

print("\n" + "="*50 + "\n")

print("Exercise 3:")

def check_even_odd(number):
   if number % 2 == 0:
       return f"{number} is even."
   else:
       return f"{number} is odd."
print(check_even_odd(4))
print(check_even_odd(7))

print("\n" + "="*50 + "\n")

print("Exercise 4:")

def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([5,5, 5]))
print("\n" + "="*50 + "\n")

print("Exercise 5:")

def print_days():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        print(day)

print_days()
print("\n" + "="*50 + "\n")

print("Exercise 6:")

def check_number (number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))

print("\n" + "="*50 + "\n")

print("Exercise 7:") 

def repeat_word(word, number):
    
    for i in range(number):
        print(word)

repeat_word("hello", 3)
print()
repeat_word("goodbye", 2)

print("\n" + "="*50 + "\n")








