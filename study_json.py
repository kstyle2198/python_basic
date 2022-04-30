# json.1oad (f): Loads JSON data from a file
# json.loads (s): Loads JSON data from a string
# json.dump(f): write JSON object to a file
# json.dumps (s) : will output a JSON object as string


import json

# loads : Loads JSON data from a string
apple_json = '{"name": "apple", "color":["red","green"], "price":"$3.45"}'
print(f"type: {type(apple_json)} result: {apple_json}")
apple_dict = json.loads(apple_json)
# keys are wrapped with single quotes
print(f"type: {type(apple_dict)} result: {apple_dict}")
print("="*50)


# load : Loads JSON data from a file
with open('secrets.json', 'r') as file:
    data = json.load(file)
print(f"type: {type(data)} result: {data}")
print("="*50)

# dumps : will output a JSON object as string
employee = {'id': '07', 'name': 'Kim', 'department': 'HR'}
json_obj = json.dumps(employee, indent=4)
print(f"type: {type(json_obj)} result: {json_obj}")
print("="*50)

# dump : write JSON object to a file
employee = {'id': '07', 'name': 'Kim', 'age': 30, 'department': 'HR'}
print(type(employee))
with open('employee.json', 'w') as outfile:
    json.dump(employee, outfile)
