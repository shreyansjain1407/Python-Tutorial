# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3,4,5,6,7,8,9,10]
fruits = ["Apples", "Orange", "Grapes", "Peach", "Pears"]
#Use a constructor
# numbers2 = list((1,2,3,4,5,6,7,8,9))

print(fruits(1))
print(len(fruits))
fruits.append("Mangoes")
fruits.remove("Pears")
fruits.insert(2, "BlueBerries")
fruits.pop(2) #Removing the element at the given location
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)
