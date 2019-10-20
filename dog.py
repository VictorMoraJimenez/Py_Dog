class Dog:
    species = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str("Dog name: " + str(self.name)+", age: "+str(self.age))

bambi = Dog("Bambi",5)
mikey = Dog("Rufus",6)

def get_biggest_number(*n):
    return max(n)

print("{} is {} and {} is {}.".format(
    bambi.name, bambi.age, mikey.name, mikey.age))


if bambi.species == "caniche":
    print("{0} is a {1}!".format(bambi.name, bambi.species))

# Create three new dogs instances
pluto = Dog("Pluto",7)
bobi = Dog("Bobi",8)
bethoven = Dog("Bethoven",9)

print(pluto)
print(bobi)
print(bethoven)

# Print the biggest dogs age 
print("The greatest age is {} years".format(get_biggest_number(pluto.age,bobi.age,bethoven.age)))



