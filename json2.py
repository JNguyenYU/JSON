#Import JSON class library
import json


#Create the data dictionary

data = {

    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['gym', 'cooking', 'videogames'],
    'is_student': False
    }

#Write data to a new file called data.json with an indentation of 4
with open('data.json', 'w') as json_file:

    json.dump(data, json_file, indent = 4)

print('Data has been written to data.json')


#
with open('data.json', 'r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

# Alter the strings
loaded_data['age'] = 34
loaded_data['interests'].append('sleep')

#
with open('data.json', 'w',) as json_file:

    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')