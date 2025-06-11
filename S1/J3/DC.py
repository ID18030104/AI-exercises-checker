class Farm:
    def __init__(self, farm_name):
        """Initialize the farm with a name and empty animals dictionary"""
        self.name = farm_name
        self.animals = {}
    
    def add_animal(self, animal_type, count=1):
        """Add animals to the farm or update existing count"""
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
    
    def get_info(self):
        """Return formatted information about the farm and its animals"""
      
        info = f"{self.name}'s farm\n\n"
        
        
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        
        info += "\n    E-I-E-I-0!"
        
        return info
    
    def get_animal_types(self):
        """Return a sorted list of all animal types on the farm"""
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        """Return a short summary of the farm's animals"""
        if not self.animals:
            return f"{self.name}'s farm has no animals."
        
        animal_types = self.get_animal_types()
        
        animal_names = []
        for animal in animal_types:
            count = self.animals[animal]
            if count > 1:
                animal_names.append(animal + "s")
            else:
                animal_names.append(animal)
        
        if len(animal_names) == 1:
            animals_text = animal_names[0]
        elif len(animal_names) == 2:
            animals_text = f"{animal_names[0]} and {animal_names[1]}"
        else:
            animals_text = ", ".join(animal_names[:-1]) + f" and {animal_names[-1]}"
        
        return f"{self.name}'s farm has {animals_text}."


print("=== Basic Test ===")
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print("\n" + "="*50)

print("\n=== Bonus Features Test ===")
print("Animal types (sorted):", macdonald.get_animal_types())
print("Short info:", macdonald.get_short_info())

print("\n=== Additional Test Cases ===")

johnson_farm = Farm("Johnson")
johnson_farm.add_animal('chicken', 20)
johnson_farm.add_animal('pig', 3)
johnson_farm.add_animal('horse', 1)
johnson_farm.add_animal('duck', 8)

print("\nJohnson's Farm Info:")
print(johnson_farm.get_info())
print(f"\nAnimal types: {johnson_farm.get_animal_types()}")
print(f"Short info: {johnson_farm.get_short_info()}")

print("\n=== Edge Cases ===")

empty_farm = Farm("Empty")
print("Empty farm info:")
print(empty_farm.get_info())
print(f"Empty farm short info: {empty_farm.get_short_info()}")

print()

single_farm = Farm("Single")
single_farm.add_animal('cow', 1)
print("Single animal farm:")
print(f"Short info: {single_farm.get_short_info()}")

two_farm = Farm("Two")
two_farm.add_animal('cow', 2)
two_farm.add_animal('pig', 1)
print(f"Two animal types: {two_farm.get_short_info()}")