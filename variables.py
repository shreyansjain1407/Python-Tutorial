# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1             #int
y = 2.5           #float
name = 'String'   #str
cooks_food = True #bool

#Multiple Assignments
# x, y, name, cooks_food =(1, 2.5, "String", True)
print ("Hello")
print (type(x))
# Type Casting
x = str(x)
y = int(y)
y = float(y)
print (type(x))

