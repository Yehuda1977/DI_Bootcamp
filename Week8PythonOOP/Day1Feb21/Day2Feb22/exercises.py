# Exercise 1: Cats
# Consider this class

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Instantiate 3 Cat objects using our class
# Create a function that finds the oldest cat and returns the cat
# Print out: “The oldest cat is , and is years old.” using the method previously created

print('Exercise #1: ===============================================')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def oldest_cat(*cats):
        oldest_cat = ''
        age = 0
        for cat in cats:
            if cat.age > age:
                age = cat.age
                oldest_cat = cat
        return oldest_cat
    @staticmethod
    def introduce_oldest(oldest_cat):
        print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old')

Whiskers = Cat("Whiskers", 15)
Mouser = Cat("Mouser", 8)
Felix = Cat("Felix", 4)

print(Cat.introduce_oldest(Cat.oldest_cat(Whiskers, Mouser, Felix)))
print(Cat.oldest_cat(Whiskers, Mouser, Felix).name)


# Exercise 2 : Dogs
# Create a class Dog.
# In this class, create a method __init__, that takes two parameters : nameand height. 
# This function instantiates two attributes, which values are the parameters.
# 1. Create a method named bark that prints “ goes woof!”
# 2. Create a method jump that prints the following “ jumps cm high!” where x is the height*2.
# 3. Outside of the class, create an object davids_dog. His dog’s name is “Rex” and his height is 50cm.
# 4. Print the details of his dog by calling the methods.
# 5. Create an object sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# 6. Print the details of her dog by calling the methods.
# 7. Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

print('Exercise #2: ===============================================')


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f'{self.name} goes woof!')
    def jump(self):
        print(f'{self.name} jumps {self.height * 2}cm high!')

davids_dog = Dog('Rex', 50)

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)


# Exercise 3 : Who’s The Song Producer ?
# 1. Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics(a list).
# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# 3. Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# 1. Then, call the method sing_me_a_song. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

print('Exercise #3: ===============================================')


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# 1. Create a class Zoo
# 2.  In this class create a method __init__ that takes one parameter: zoo_name
#     It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# 3. Create a method add_animal that takes one parameter new_animal. 
#     This method adds the new_animal to the animals list, only if the new_animal isn’t already in the list.
# 4. Create a method get_animals that prints all the of animals in the zoo.
# 5. Create a method sell_animal that takes one parameter animal_sold. 
#    This method removes the animal from the list, only if he was already in the list.
# 6. Create a method sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
# 1. Create a method get_groups that prints the animal/animals inside each group.
# 2. Create an object ramat_gan_safari and call all the methods.
# Tip: for each method, the argument should be the answer of the zoo keeper.
# Example

# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

print('Exercise #4: ===============================================')


class Zoo:
    animals = []
    group_animals = {}
    def __init__(self, zoo_name):
        name = zoo_name
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f'Added {new_animal} successfully.')
        else:
            print('Sorry, that animal is already in the list.')
    def get_animals(self):
        print('Listing animals:')
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            print(f'Removed {animal_sold} successfully.')
            self.animals.remove(animal_sold)
        else:
            print(f'{animal_sold} is not in your zoo.')
    def sort_animals(self):
        self.animals.sort()
        for animal in self.animals:
            if animal[0] not in self.group_animals.keys():
                self.group_animals.update({animal[0]:[animal]})
            else:  
                self.group_animals[animal[0]].append(animal)
        
        print(self.group_animals)


ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Dinosaur')
ramat_gan_safari.add_animal('Elephant')
ramat_gan_safari.add_animal('Cow')
ramat_gan_safari.add_animal('Seal')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Seal')
ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal('Dingo')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Emu')
ramat_gan_safari.sort_animals()