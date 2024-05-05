# Define a dictionary representing workmates
workmates_dict = {
    150: "Maxwell Barno",
    230: "Khadija Mganda",
    340: "Naomi Munyiri",
    450: "Brian Kipkosgei",
    1000: ["Mike", "Luke", "John"]
}

# Accessing a specific value in the dictionary
print(workmates_dict[150])

# Adding new key-value pairs to the dictionary
workmates_dict[680] = "Nick Ochieng"
workmates_dict[760] = "Kevin Mwaniki"

# Printing the dictionary after modifications
print(workmates_dict)

# Retrieving the list of names from the dictionary
names_list = workmates_dict[1000]
print(len(names_list))

# Printing the length of the keys in the dictionary
print(len(workmates_dict.keys()))

# Iterating through the dictionary
#Printing all keys one by one
for mate in workmates_dict:
    print(mate)

# Printing all values one by one
for mates in workmates_dict:
    people = workmates_dict[mates]
    print(people)

# Method to retrieve all keys
print(workmates_dict.keys())

# Method to retrieve all values
print(workmates_dict.values())

# Method to print both keys and values
print(workmates_dict.items())

# Iterating through the dictionary to print keys and values
for key, value in workmates_dict.items():
    print(f"{key}={value}")

# Method to retrieve a specific value using its key
team_lead = workmates_dict.get(150)
print(team_lead)

# Deleting a key-value pair from the dictionary
del workmates_dict[150]
print(workmates_dict)

# Another way to delete a key-value pair using pop() method
workmates_dict.pop(340)
print(workmates_dict)

# Nested dictionaries representing family members
my_family = {
    "child0": {
        "name": "Milo",
        "year": 1990,
    },
    "child1": {
        "name": "Mariah",
        "year": 2000
    },
    "child2": {
        "name": "Jayden",
        "year": 2012
    }
}

# Accessing a specific value in the nested dictionary
print(my_family["child1"]["name"])

# Iterating through the nested dictionary to print keys and values
for key, obj in my_family.items():
    print(key, obj)
