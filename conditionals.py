# If/ Else conditions are used to decide to do something based on something being true or false

x = 15
y = 10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f"{x} is greater than {y}")

#If Else
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")
# Logical operators (and, or, not) - Used to combine conditional statements
if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} is equal to {y}")

#Nested Statements
if x > y:
    if x > 5:
        print(f"{x} is greater than {y} and 5")

if x > y and x > 5: #or 
    print(f"{x} is greater than {y} and 5")

if not (x == y):
    print(f"{x} is not equal {y}")

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5,6,7,8,9]
if 3 in numbers: #not in
    print("3 is present in the list numbers")

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if 15 is 15: #is not
    print("Something")