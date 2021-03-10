import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# 1 Access the nested key “salary” from the above JSON-string
# 2 Add a key “birth_date” at the same level of the key “name”
# 3 Save the dictionary as JSON to a file

info = json.loads(sampleJson)
print(info['company']['employee']['payable']['salary'])
info['company']['employee']['birth_date'] = ''
print(info)
print(type(info))

json_info = json.dumps(info)
print(type(json_info))

json_file = 'output.json'

with open(json_file, 'w') as f:
    json.dump(info, f, indent = 2, sort_keys=True)