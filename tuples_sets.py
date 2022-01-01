# A Tuple is a collection which is ordered and UNCHANGEABLE. Allows duplicate members.
 
#Creation
fruits = ("Apples", "Orange", "Grapes")

# fruits2 = tuple(fruits)
# print(fruits, fruits2)


# A Set is a collection which is unordered and unindexed. No duplicate members.
#Creation
fruits_set = {"Apples", "Orange", "Grapes", "Mango"}
print("Apples" in fruits_set) #Boolean
fruits_set.add("Grapes")
fruits_set.remove("Grapes")

#Clear set
fruits_set.clear()