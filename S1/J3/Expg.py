import math
import random


print("="*50)
print("EXERCISE 1: GEOMETRY")
print("="*50)

class Circle:
    def __init__(self, radius=1.0):
        """Initialize a circle with a given radius (default 1.0)"""
        self.radius = radius
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius
    
    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * self.radius ** 2
    
    def definition(self):
        """Print the geometrical definition of a circle"""
        print("A circle is a round shape with all points at an equal distance from the center.")
        print("The distance from the center to any point on the circle is called the radius.")

circle1 = Circle()  
circle2 = Circle(5)  
print(f"Circle 1 (radius {circle1.radius}):")
print(f"  Perimeter: {circle1.perimeter():.2f}")
print(f"  Area: {circle1.area():.2f}")

print(f"\nCircle 2 (radius {circle2.radius}):")
print(f"  Perimeter: {circle2.perimeter():.2f}")
print(f"  Area: {circle2.area():.2f}")

print("\nGeometrical definition:")
circle1.definition()

print("\n" + "="*50)
print("EXERCISE 2: CUSTOM LIST CLASS")
print("="*50)

class MyList:
    def __init__(self, letters):
        """Initialize MyList with a list of letters"""
        self.letters = letters
    
    def reversed_list(self):
        """Return the reversed list"""
        return self.letters[::-1]
    
    def sorted_list(self):
        """Return the sorted list"""
        return sorted(self.letters)
    
    def random_list(self):
        """Bonus: Generate a second list with random numbers, same length as original list"""
        return [random.randint(1, 100) for _ in range(len(self.letters))]

my_letters = MyList(['z', 'a', 'c', 'b', 'y', 'x'])

print(f"Original list: {my_letters.letters}")
print(f"Reversed list: {my_letters.reversed_list()}")
print(f"Sorted list: {my_letters.sorted_list()}")
print(f"Random list (same length): {my_letters.random_list()}")

print("\n" + "="*50)
print("EXERCISE 3: RESTAURANT MENU MANAGER")
print("="*50)

class MenuManager:
    def __init__(self):
        """Initialize the menu with current dishes"""
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]
    
    def add_item(self, name, price, spice, gluten):
        """Add a new dish to the menu"""
        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(f"'{name}' has been added to the menu!")
    
    def update_item(self, name, price, spice, gluten):
        """Update an existing dish or notify if not found"""
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"'{name}' has been updated!")
                return
        print(f"'{name}' is not in the menu and cannot be updated.")
    
    def remove_item(self, name):
        """Remove a dish from the menu or notify if not found"""
        for i, dish in enumerate(self.menu):
            if dish["name"].lower() == name.lower():
                removed_dish = self.menu.pop(i)
                print(f"'{removed_dish['name']}' has been removed from the menu!")
                self.display_menu()
                return
        print(f"'{name}' is not in the menu and cannot be removed.")
    
    def display_menu(self):
        """Display the current menu (helper method)"""
        print("\nCurrent Menu:")
        print("-" * 60)
        for dish in self.menu:
            gluten_text = "Contains Gluten" if dish["gluten"] else "Gluten-Free"
            spice_text = {"A": "Not Spicy", "B": "A Little Spicy", "C": "Very Spicy"}[dish["spice"]]
            print(f"{dish['name']:<20} - ${dish['price']:<3} - {spice_text:<15} - {gluten_text}")
        print("-" * 60)

restaurant = MenuManager()

print("Initial Menu:")
restaurant.display_menu()

print("\nTesting add_item:")
restaurant.add_item("Pasta", 12, "A", True)
restaurant.add_item("Spicy Wings", 8, "C", False)

print("\nTesting update_item:")
restaurant.update_item("Soup", 12, "A", False)  
restaurant.update_item("Pizza", 20, "B", True)  

print("\nTesting remove_item:")
restaurant.remove_item("French Fries")  
print("\nTrying to remove non-existing item:")
restaurant.remove_item("Sushi")  

print("\nFinal Menu:")
restaurant.display_menu()

print("\n" + "="*50)
print("ADDITIONAL DEMONSTRATIONS")
print("="*50)


print("\nCircle Examples:")
circles = [Circle(3), Circle(7.5), Circle(10)]
for i, circle in enumerate(circles, 1):
    print(f"Circle {i} (radius {circle.radius}):")
    print(f"  Perimeter: {circle.perimeter():.2f}")
    print(f"  Area: {circle.area():.2f}")


print("\nMyList Examples:")
word_list = MyList(['h', 'e', 'l', 'l', 'o'])
print(f"Letters: {word_list.letters}")
print(f"Reversed: {word_list.reversed_list()}")
print(f"Sorted: {word_list.sorted_list()}")
print(f"Random numbers: {word_list.random_list()}")

