class Farm:
    animals = {}
    
    def __init__(self, name):
        self.name = name
        print(f'{name} Farm has been created')
    def get_info(self):
        print('E-I-E-I-O!')
    def add_animal(self, new_animal, number=1):
        if new_animal not in self.animals:
            self.animals.update({new_animal:number})
            print(f'Added {number} {new_animal}(s) successfully.')
        else:
            new_total = self.animals.get(new_animal) + number 
            self.animals.update({new_animal:new_total})
            print(f'{number} {new_animal}(s) has/ve been added successfully for a total of {new_total} {new_animal}s')
    def list_animals(self):
        for animal in self.animals:
            print(f'{animal}: {self.animals[animal]}')
    def get_animal_types(self):
        animal_types = []
        print('These are all the animal types:')
        for key in self.animals.keys():
            animal_types.append(key)
        animal_types.sort()
        print(animal_types)
        return animal_types
    def get_short_info(self):
        short_info = ('(s), ').join(self.get_animal_types())
        print(f'{self.name} has {short_info}(s).')
        
        

McDonalds = Farm('McDonalds')
McDonalds.get_info()
McDonalds.add_animal('Goat', 25)
McDonalds.add_animal('Donkey')
McDonalds.add_animal('Donkey')
McDonalds.add_animal('Chicken', 14)
McDonalds.add_animal('Horse')
McDonalds.add_animal('Pig', 2)
McDonalds.list_animals()
McDonalds.get_animal_types()
McDonalds.get_short_info()