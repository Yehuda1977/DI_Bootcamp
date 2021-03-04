""" Exercise 1
Create a class Human, it has the following attributes:

name (str)
age (int)
living_place (Building - Default is None)
Create another class Building, it has the following attributes:

address (str)
inhabitants (List of Human objs - Default is empty)
Create a class City, it has the following attributes:

name (str)
buildings (List of Building objs - Default is empty)
Add the move(self, building) method to the Human class, 
it sets the living place of this human to the building and add this human to the building inhabitants.
Add the construct(self, address) method to the City class, it adds a building at the referenced address.
Add the info(self, address) method to the City class, 
it displays the number of buildings and the mean age of the citizens.

 """
import statistics

class Human():
    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building.address
        building.inhabitants.append(self)

class Building():
    def __init__(self, address, inhabitants=[]):
        self.address = address
        self.inhabitants = inhabitants

class City():
    def __init__(self, name, buildings=[]):
        self.name = name
        self.buildings = buildings
    def construct(self, building):
        self.buildings.append(building)
    def info(self):
        num_buildings = len(self.buildings)
        ages = []
        for building in self.buildings:
            for human in building.inhabitants:
                ages.append(human.age)
        average_age = statistics.mean(ages)
        print(f'There is/are {num_buildings} building(s) in {self.name}')
        print(f'The average age of the inhabitants is {average_age}')
        



b = Building('7 Freeport Rd')

h = Human('Jon', 4, 'California')
i = Human('Phil', 20, 'NY')
j = Human('Paul', 1, 'NY')
k = Human('Bill', 90, 'NY')

d = Building('9 Freeport Rd')

l = Human('Carl', 4, 'California')
m = Human('Will', 12, 'NY')
n = Human('Sam', 1, 'NY')
o = Human('Sue', 52, 'NY')

l.move(b)
m.move(b)
n.move(b)
o.move(b)

c = City('NY')

c.construct(b)
c.construct(d)

""" def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_living_place(self):
        return self.__living_place

    def set_name(self, name):
        self.__name = name if isinstance(name, str) else TypeError and print(f'Error, {name} is incorrect type')
        
    def set_age(self, age):
        self.__age = age if isinstance(age, int) else TypeError and print(f'Error, {age} is incorrect type')
       
    def set_living_place(self, living_place):
        self.__living_place = living_place if isinstance(living_place, str) else TypeError and print(f'Error, {living_place} is incorrect type')
         """