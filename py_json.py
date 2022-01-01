# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#Sample
userJSON = '{"fname":"Shreyans","lname":"Jain", "age":"23"}'

#parse to dictionary
user = json.loads(userJSON)

print(user)

car = {'manufacturer':'volkswagen', 'model':'polo', 'year':'2019'}
carJSON = json.dumps(car)
print(carJSON)