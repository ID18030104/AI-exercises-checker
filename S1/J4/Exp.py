print ("="*50)
print("Exercise 1")
print("="*50)

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def __init__(self, name, age, eye_color="blue"):
        super().__init__(name, age)
        self.eye_color = eye_color

    def purr(self):
        return f"{self.name} is purring with elegance."


bengal = Bengal("Simba", 3)
chartreux = Chartreux("Felix", 5)
siamese = Siamese("Luna", 2)

all_cats = [bengal, chartreux, siamese]


sara_pets = Pets(all_cats)


sara_pets.walk()



print("\n" + "="*50)
print("Exercise 2")
print("="*50)

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        opponent_power = other_dog.run_speed() * other_dog.weight
        if my_power > opponent_power:
            return f"{self.name} won the fight"
        elif opponent_power > my_power:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie!"


dog1 = Dog("Rex", 4, 20)
dog2 = Dog("Buddy", 6, 25)
dog3 = Dog("Max", 3, 18)


print(dog1.bark())
print(f"{dog2.name}'s run speed: {dog2.run_speed()}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))

print("\n" + "="*50)
print("Exercise 3")
print("="*50)


import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        opponent_power = other_dog.run_speed() * other_dog.weight
        if my_power > opponent_power:
            return f"{self.name} won the fight"
        elif opponent_power > my_power:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie!"


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

pet_dog1 = PetDog("Fido", 2, 10)
pet_dog2 = PetDog("Buddy", 4, 14)
pet_dog3 = PetDog("Max", 3, 12)

pet_dog1.train()  
pet_dog1.play(pet_dog2, pet_dog3)  
pet_dog1.do_a_trick()  


print("\n" + "="*50)
print("Exercise 4")
print("="*50)


class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

# Step 2: Create the Family Class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("No such family member found.")

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, age {member.age}")


smith_family = Family("Smith")
smith_family.born("Alice", 17)
smith_family.born("Bob", 20)
smith_family.check_majority("Alice")
smith_family.check_majority("Bob")
smith_family.family_presentation()