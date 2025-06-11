import random

print("=== Exercise 1: Birthday Look-up ===")

birthdays = {
    "Alice": "1995/03/15",
    "Bob": "1987/12/22",
    "Charlie": "1992/07/08",
    "Diana": "1990/11/03",
    "Eve": "1988/05/17"
}

print("Welcome to the Birthday Look-up!")
print("You can look up the birthdays of the people in the list!")

name = input("Enter a person's name: ")

birthday = None
actual_name = None
for person in birthdays:
    if person.lower() == name.lower():
        birthday = birthdays[person]
        actual_name = person
        break


if birthday:
    print(f"{name}'s birthday is {birthday}")
else:
    print(f"Sorry, we don't have birthday information for {name}")

print()


print("=== Exercise 2: Birthdays Advanced ===")

print("People in our birthday list:")
for person in birthdays.keys():
    print(f"- {person}")

name = input("\nEnter a person's name: ")
birthday = None
actual_name = None
for person in birthdays:
    if person.lower() == name.lower():
        birthday = birthdays[person]
        actual_name = person
        break


if birthday:
    print(f"{name}'s birthday is {birthday}")
else:
    print(f"Sorry, we don't have the birthday information for {name}")

print()


print("=== Exercise 3: Check the index ===")

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    index = names.index(user_name)
    print(f"The index of the first occurrence of '{user_name}' is {index}")
else:
    print(f"'{user_name}' is not in the names list")

print()


print("=== Exercise 4: Double Dice ===")

def throw_dice():
    """Simulate rolling a dice, returns integer between 1 and 6"""
    return random.randint(1, 6)

def throw_until_doubles():
    """Keep throwing 2 dice until doubles are reached, return number of throws"""
    throws = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws += 1
        
        if dice1 == dice2:
            break
    
    return throws

def main():
    """Main function that throws doubles 100 times and calculates statistics"""
    results = []  
    
    
    for i in range(100):
        throws_needed = throw_until_doubles()
        results.append(throws_needed)
    
    total_throws = sum(results)
    
    average_throws = total_throws / len(results)
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

main()