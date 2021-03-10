import json

my_family = {
    "parents" :['Beth', 'Jerry'],
    "children" :['Summer', 'Morty']
}

print(type(my_family))
json_file = "index.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)