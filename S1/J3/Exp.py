print("=== Exercise 1: Cats ===")

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Whiskers", 5)
cat2 = Cat("Mittens", 8)
cat3 = Cat("Shadow", 3)

def find_oldest_cat(cat1, cat2, cat3):
    cats = [cat1, cat2, cat3]
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

print()

print("=== Exercise 2: Dogs ===")

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Buddy", 30)
sarahs_dog = Dog("Luna", 25)


print(f"David's dog: {davids_dog.name}, height: {davids_dog.height} cm")
print(f"Sarah's dog: {sarahs_dog.name}, height: {sarahs_dog.height} cm")

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()


if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}")
else:
    print("Both dogs are the same height")

print()

print("=== Exercise 3: Song ===")

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()

print()

print("=== Exercise 4: Zoo ===")

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo")
    
    def get_animals(self):
        print(f"Animals in {self.zoo_name}:")
        for animal in self.animals:
            print(f"- {animal}")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold")
        else:
            print(f"{animal_sold} is not in the zoo")
    
    def sort_animals(self):
        
        sorted_animals = sorted(self.animals)
        
        
        groups = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        
        return groups
    
    def get_groups(self):
        groups = self.sort_animals()
        print("Animals grouped by first letter:")
        for letter, animal_list in groups.items():
            print(f"{letter}: {animal_list}")


ramat_gan_safari = Zoo("Ramat Gan Safari")


print("Adding animals...")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")

print()
ramat_gan_safari.get_animals()

print()
print("Selling Bear...")
ramat_gan_safari.sell_animal("Bear")

print()
ramat_gan_safari.get_animals()

print()
ramat_gan_safari.get_groups()

