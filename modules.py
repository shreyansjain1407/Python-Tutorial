# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

## Core Python modules
import datetime #*
from datetime import date #**
import time
#Once a module has been installed using pip, you can import it
from camelcase import CamelCase

#Import custom modules
import validator

today = datetime.date.today() #*
today = date.today() #**
print(today)

timestamp = time.time()
print(timestamp)

c = CamelCase()
print(c.hump("hello world everything is capitalized"))

email = "test@test.com"
if validator.validate_email(email):
    print("Email is valid")