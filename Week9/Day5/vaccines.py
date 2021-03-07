# Vaccines Management System
# Your goal is to create a program to help a city with the vaccination of its citizens.

# Part 1
# You will have to create two classes:

# Human
# Queue
# Here is a description of them:

# 1) Human
# Represents a citizen of the city, it has the following attributes: 
# id_number (str), 
# name (str), 
# age (int), 
# prioritary (bool) and 
# blood_type (str). 
# Its blood type can be “A”, “B”, “AB” or “O”.

# It got no methods.

# 2) Queue
# Represents a queue of humans waiting for their vaccine. 
# It has two attributes, humans, the list containing the humans that are waiting, it is initialized empty.
# This class is useful to manage who will get vaccinated in priority. 
# It has the following methods:

# add_person(self, person) Add a human to the queue, if he is older than 60 years old or a prioritary person, 
# put him at the beginning of the list (at index 0) before every other.
# find_in_queue(self, person) Returns the index of a human in the queue.
# swap(self, person1, person2) Swaps person1 with person2.
# get_next(self) return the next human in the queue, meaning the object at index 0 in the list.
# get_next_blood_type(self, blood_type) Return the first human with this specific blood type.
# sort_by_age(self) Sort the queue so that the older ones are before the younger ones and all the prioritary persons are before the others.
# Every human returned by get_next and get_next_blood_type is removed from the list, those functions return None if there is no one in the list.

# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.

class Human():
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

class Queue():
    def __init__(self, humans = []):
        self.humans = humans
    def add_person(self, person):
        if person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
    def find_in_queue(self, person):
        return self.humans.index(person)
    def swap(self, person1, person2):
        index_1 = self.find_in_queue(person1)
        index_2 = self.find_in_queue(person2)
        self.humans[index_1] = person2
        self.humans[index_2] = person1
    def get_next(self):
        if self.humans:
            print(self.humans[0].name)
            return self.humans.pop(0)
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for person in self.humans:
            if person.blood_type == blood_type:
                print(person.name)
                index = self.humans.index(person)
                return self.humans.pop(index)
            else:
                return 'None found'
    def sort_by_age(self):
        copy_list = self.humans
        sorted = []
        
        while copy_list:
            max = copy_list[0]
            for person in copy_list:
                if person.age > max.age:
                    max = person
            sorted.append(max)
            copy_list.remove(max)

        # for human in sorted:
        #     print(human.name, human.age)

        for human in sorted:
            if human.priority == True:
                human_to_move = human
                sorted.remove(human)
                sorted.insert(0, human_to_move)

        for human in sorted:
            print(human.name, human.age)
        # for human in self.humans:
        #     list_to_sort.append({f'{human.age}' : f'{human.id_number}' })
        # for human in self.humans:
        #     ages_to_sort.append(human.age)
        # ages_to_sort.sort(reverse=True)
        # print(ages_to_sort)

    

            
        

h = Human('a', 'Fred', 21, True, 'A')
i = Human('b', 'Jon', 62, False, 'B')
j = Human('c', 'Bob', 32, True, 'AB')
k = Human('d', 'Mary', 43, False, 'O')
l = Human('e', 'Joe', 65, True, 'A')

q = Queue()

q.add_person(h)
q.add_person(i)
q.add_person(j)
q.add_person(k)
q.add_person(l)

print('\nOriginal queue:\n')
for human in q.humans:
    print(human.name)

q.swap(h, i)

print('\nQueue after swap\n')
for human in q.humans:
    print(human.name)

# print('\nGet next:')
# print(q.get_next().name)

# print('\nIndex of blood type:')
# print(q.get_next_blood_type('A'))

# Part 2
# Create an attribute family for the Human class. 
# Initialized as empty, family is a list of all the humans 
# that are living in the same house with this human. 
# Add a method add_family_member(self, person) 
# that adds the person to this human’s family and this human to the person’s family.

# Add the rearange_queue(self) method to the Queue class, 
# so that there is no two members of the same family one after the other.


class Family():
    def __init__(self, humans = []):
        self.humans = humans
    def add_family_member(self, person):
        self.humans.append(person)