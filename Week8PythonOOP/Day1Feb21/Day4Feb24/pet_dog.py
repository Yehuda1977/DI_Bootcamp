# Exercise 3 : Dogs Domesticated
# 1. Create a new python file and import your Dog class from the previous exercise.
# 2. Create a class named PetDog that inherits from Dog.
# 3. Add the attribute trained (boolean) to the PetDog class, should always start False
# 4. Add the following methods:
#   train: prints the output of bark and switches the trained boolean to True
#   play: gets parameter of any amount of other dogs (look up args) and prints “the dogs: dog_names play together” each of the dogs that plays has their trained boolean switched to False
#   do_a_trick: will print one of the following sentences randomly ONLY IF the dogs trained boolean is True, after doing the trick the trained boolean moves to False
#       “dog_name does a barrel roll”
#       “dog_name stands on their back legs”
#       “dog_name shakes your hand”
#       “dog_name plays dead”

print('Exercise 3================================\n')


import './exercises.py'

class PetDog(Dog):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
        self.trained = False 

    def trained(self):
        print(self.bark())
        self.trained = True

    def play(self, other_dogs):
        dog_names = ""

        for dog in other_dogs:
            dog_names += dog.name + '+'
            dog.trained = False

