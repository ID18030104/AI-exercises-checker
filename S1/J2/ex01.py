print("=== Exercise 1: Converting Lists into Dictionaries ===")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Solution avec zip()
result_dict = dict(zip(keys, values))
print(f"Résultat: {result_dict}")



print("=== Exercise 2: Cinemax #2 ===")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

total_cost = 0
for name, age in family.items():
    price = calculate_ticket_price(age)
    print(f"{name.title()} ({age} ans): ${price}")
    total_cost += price

print(f"Coût total: ${total_cost}")

# bonus
print("\n--- Bonus ---")
def interactive_cinema():
    family_input = {}
    while True:
        name = input("Entrez le nom du membre de la famille (ou 'stop' pour terminer): ")
        if name.lower() == 'stop':
            break
        try:
            age = int(input(f"Entrez l'âge de {name}: "))
            family_input[name] = age
        except ValueError:
            print("Veuillez entrer un âge valide.")
    
    total = 0
    for name, age in family_input.items():
        price = calculate_ticket_price(age)
        print(f"{name.title()} ({age} ans): ${price}")
        total += price
    
    print(f"Coût total: ${total}")


interactive_cinema()

print()

print("=== Exercise 3: Zara ===")
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# 1. 
brand["number_stores"] = 2

# 2.
clothes_types = ", ".join(brand["type_of_clothes"])
print(f"Zara crée des vêtements pour: {clothes_types}")

# 3.
brand["country_creation"] = "Spain"

# 4. 
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 5. 
brand.pop("creation_date", None)

# 6. 
print(f"Dernier concurrent: {brand['international_competitors'][-1]}")

# 7. 
print(f"Couleurs principales aux US: {brand['major_color']['US']}")

# 8. 
print(f"Nombre de clés: {len(brand)}")

# 9. 
print(f"Toutes les clés: {list(brand.keys())}")

# Bonus: 
more_on_zara = {"creation_date": 1975, "number_stores": 7000}
brand.update(more_on_zara)
print(f"Dictionnaire fusionné: {brand}")

print()

print("=== Exercise 4: Some Geography ===")
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")


print("=== Exercise 5: Random ===")
import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success! Your number {user_number} matches the random number {random_number}.")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")


compare_numbers(50)
compare_numbers(10)
compare_numbers(25)
compare_numbers(75)
compare_numbers(100)
compare_numbers(7)
compare_numbers(12)


print()

print("=== Exercise 6: Personalized Shirt ===")

def make_shirt(size="large", text="I love Python"):
    print(f"The size is {size} and the text: '{text}'")
make_shirt()
make_shirt("medium")
make_shirt("small", "Custome Message")

make_shirt(size="Small", text="Hello !")
make_shirt(text="Bonjour !", size="Extra Large")
print()


print("=== Exercise 7: Temperature Advice ===")

import random

def get_random_temp():
    return random.randint(-10, 40)

def get_random_temp_float():
    return round(random.uniform(-10, 40), 1)

def get_advice(temp):
    if temp < 0:
        return "Brrr, that's freezing! Wear some extra layers today."
    elif 0 <= temp <= 16:
        return "Quite chilly! Don't forget your coat."
    elif 16 < temp <= 23:
        return "Nice weather."
    elif 24 <= temp <= 32:
        return "A bit warm, stay hydrated."
    else:
        return "It's really hot! Stay cool."

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    print(get_advice(temp))

def main_float():
    temp = get_random_temp_float()
    print(f"The temperature right now is {temp} degrees Celsius.")
    print(get_advice(temp))


main()


print("\n--- Version avec températures flottantes ---")
main_float()


print("\n--- Bonus: Version avec saisons ---")
def get_seasonal_temp(month):
    if month in [12, 1, 2]:  # Hiver
        return random.randint(-10, 5)
    elif month in [3, 4, 5]:  # Printemps
        return random.randint(5, 20)
    elif month in [6, 7, 8]:  # Été
        return random.randint(20, 40)
    else:  # Automne (9, 10, 11)
        return random.randint(5, 18)

def seasonal_main():
    try:
        month = int(input("Entrez le mois (1-12): "))
        if 1 <= month <= 12:
            temp = get_seasonal_temp(month)
            seasons = {
                (12, 1, 2): "hiver",
                (3, 4, 5): "printemps", 
                (6, 7, 8): "été",
                (9, 10, 11): "automne"
            }
            season = next(s for months, s in seasons.items() if month in months)
            print(f"En {season}, la température est de {temp} degrés Celsius.")
            print(get_advice(temp))
        else:
            print("Veuillez entrer un mois entre 1 et 12.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")


seasonal_main()

print()

print("=== Exercise 8: Pizza Toppings ===")
def pizza_ordering():
    toppings = []
    base_price = 10
    topping_price = 2.50
    
    print("Bienvenue! Ajoutez vos garnitures de pizza (tapez 'quit' pour terminer):")
    
    while True:
        topping = input("Entrez une garniture: ").strip()
        if topping.lower() == 'quit':
            break
        if topping:  
            toppings.append(topping)
            print(f"Adding {topping} to your pizza.")
    
    if toppings:
        total_cost = base_price + (len(toppings) * topping_price)
        print(f"\nVos garnitures: {', '.join(toppings)}")
        print(f"Prix de base: ${base_price}")
        print(f"Garnitures ({len(toppings)} x ${topping_price}): ${len(toppings) * topping_price}")
        print(f"Coût total: ${total_cost}")
    else:
        print(f"\nPizza nature - Coût total: ${base_price}")


def pizza_demo():
    toppings = ["pepperoni", "mushrooms", "olives"]
    base_price = 10
    topping_price = 2.50
    
    print("Démonstration de commande de pizza:")
    for topping in toppings:
        print(f"Adding {topping} to your pizza.")
    
    total_cost = base_price + (len(toppings) * topping_price)
    print(f"\nVos garnitures: {', '.join(toppings)}")
    print(f"Prix de base: ${base_price}")
    print(f"Garnitures ({len(toppings)} x ${topping_price}): ${len(toppings) * topping_price}")
    print(f"Coût total: ${total_cost}")


pizza_demo()
pizza_ordering()