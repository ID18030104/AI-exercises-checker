print("Exercise 001")   
print("Hello world\nHello world\nHello world\nHello world")

print(print("\n" + "="*50 + "\n"))

print("Exercise 002")
result = (99 ** 3) * 8
print(result)
print(print("\n" + "="*50 + "\n"))

print("Exercise 003")

my_name = "Isaac" 
user_name = input("What is your name? ")

if user_name == my_name:
    print("Wow! We have the same name! Are we twins?! ")
else:
    print(f"Nice to meet you, {user_name}! But my name is way cooler than yours, it's {my_name}!")
print(print("\n" + "="*50 + "\n"))

print("Exercise 004")

hight = float(input("Enter your height in cm: "))
if hight < 145:
    print("You are too short to ride this roller coaster.")
else: 
    print("You are tall enough to ride this roller coaster. Enjoy the ride!")
print(print("\n" + "="*50 + "\n"))

print("Exercise 005")

my_fav_numbers = [3, 7, 9, 11, 13]
my_fav_numbers.append(17)
my_fav_numbers.append(19)
my_fav_numbers.remove(3)
print(my_fav_numbers)

friend_fav_numbers = [2, 4, 6, 8, 10]
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

print(print("\n" + "="*50 + "\n"))

print("Exercise 006")

my_tuple = (1, 2, 3)
try:
    my_tuple.append(4)
except AttributeError:
    my_tuple = my_tuple + (4,)
print(my_tuple)
print("Tuples are immutable, so you can't add items to them once created.")

print(print("\n" + "="*50 + "\n"))

print("Exercise 007")

basket = ["apple", "banana", "orange", "bluberry"]
basket.remove("bluberry", "banana")
basket.append("kiwi")
basket.instert(0, "apple")
apple_count = basket.count("apple")
print(f"There are {apple_count} apples in the basket.")

basket.clear()
print("The basket is now empty:", basket)

print(print("\n" + "="*50 + "\n"))

print("Exercise 008")

sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
    "Pastrami sandwich"
]

print("Sorry, the deli has run out of pastrami.\n")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich.lower()}")
    finished_sandwiches.append(sandwich)



