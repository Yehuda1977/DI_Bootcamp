# Exercise 1
print('Exercise 1===================================')

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for item in zip(keys, values): # only go as far it is possible
    print(item)

# Exercise 2
print('Exercise 2===================================')

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0
for (person, age) in family.items():
    if age < 3:
        print(f"{person}'s ticket is free")
    elif 3 < age < 12:
        print(f"{person}'s ticket is $10")
        total+=10
    else:
        print(f"{person}'s ticket is $15")
        total+=15
print(total)


# Exercise 3
print('Exercise 3===================================')
brand = {

    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ['men', 'women', 'children', 'home'],
    "international_competitors": ['Gap', 'H&M', 'Benetton'],
    "number_stores": 7000,
    "major_color": { 
        "France": "blue", 
        "Spain": "red", 
        "US":['pink', 'green']
    }
}

print(f'The number of stores is {brand["number_stores"]}') 
brand["number_stores"] = 2
print(f'The number of stores is {brand["number_stores"]}') 

print(f'The clients of {brand["name"]} are ')
for client in brand["type_of_clothes"]:
    print(client)

brand["country_creation"] = "Spain"
print(brand["country_creation"])

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
for company in brand["international_competitors"]:
    print(company)

del brand["creation_date"]

print(brand["international_competitors"][-1])

separator = ', '
color_clothes = separator.join(brand["major_color"]["US"])
print(f'The major clothes colors in the US are: {color_clothes}')

count = 0
for key in brand:
    count+=1
print(count)

