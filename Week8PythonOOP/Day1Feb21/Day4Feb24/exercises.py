# Consider this code

class Pets():
    animals = []
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
# Add another cat breed
# Create a list of all of the pets (create 3 cat instances from the above) my_cats = []
# Instantiate the Pet class with all your cats. Use the variable my_pets
# Output all of the cats walking using the my_pets instance

class Tabby(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bennie = Bengal('Bennie', 5)
print(bennie.sing('meow'))
print(bennie.name)
print(bennie.age)


# Exercise 2 : Dogs
# 1. Create a class named Dog with the attributes name, age, weight
# 2. Implement the following methods for the class:
# -bark: returns a string of “ barks”.
# -run_speed: returns the dogs running speed (weight/age *10).
# -fight : gets parameter of other_dog, returns string of which dog won the fight between them, 
# whichever has a higher run_speed x weight should win.
# 3. Create 3 dogs and use some of your methods
print('Exercise 2================================\n')


class Dogs():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f'"Bark, bark, bark", says {self.name}'
    def run_speed(self):
        return (self.weight / self.age) * 10
    def fight(self, other_dog):
        return self.name if (self.run_speed() > other_dog.run_speed()) else other_dog.name

rufus = Dogs('Rufus', 12, 55)
fido = Dogs('Fido', 1, 25)
barklee = Dogs('Barklee', 8, 40)

print(rufus.run_speed())
print(fido.run_speed())
print(barklee.run_speed())

print(rufus.fight(fido))

print(rufus.bark())




