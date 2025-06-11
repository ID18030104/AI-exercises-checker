print("Hello, world !")

def say_hello ():
    print ("Hello, world !")
    
say_hello()

def say_hello ():
    return("Hello, World !")

print (say_hello())  

def introduce_pet(cat_name, dog_name):
    return f"I have a cat named {cat_name} and a dog named {dog_name}."


print(introduce_pet("Mittens", "Fido"))


print(introduce_pet(dog_name="Fido", cat_name="Mittens"))

def greet_person(name, age):
    return f"Hello {name}, you are {age} years old."

def greet_person(name, age=30):
    return f"Hello {name}, you are {age} years old."

print(greet_person("Alice", 25))
print(greet_person("Bob"))