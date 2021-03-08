# Exercise 6 : Faker Module
# Install the faker module, and read the documentation.
# Create an empty list called users. Tip: It’s a list of dictionaries
# Create a function that adds dictionaries to the users list. 
# Each user has the properties: name, adress, langage_spoken. 
# Use faker to populate them with fake data.

from faker import Faker
fake = Faker()

user_list = []

def add_user(user_list):
    name =fake.name()
    address = fake.address()
    user = {
        'name': name, 
        'address': address
    }
    user_list.append(user)

for i in range(0, 100):
    add_user(user_list)

for user in user_list:
    print(user['name'], user['address'])