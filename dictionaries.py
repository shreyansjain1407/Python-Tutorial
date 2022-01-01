# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#Creation
person = {
    "FName": "Shreyans",
    "LName": "Jain",
    "Age": 23
}

print(person, type(person))

print(person["FName"])
print(person.get("LName"))

#Addition
person['Phone'] = "3528715403"
print(person, type(person))

#Get keys and items
print(person.keys())
print(person.items())

#Copy a dictionary
person2 = person.copy()
person2['city'] = 'boston'

#Remove Item
del(person2['city']) #Case sensitive
person.pop('Age')

#Len function is applicable to th as well

#List of dictionaries
people = [
    {'name':"S", 'age':"23"},
    {'name':"K", 'age':"23"},
    {'name':"R", 'age':"23"}
]