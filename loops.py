# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['SJ', 'KB', 'RG', 'GV', 'RN']

#Simple for loop
for person in people:
    print(f"Current person: {person}")

#break and continue
for person in people:
    if person is 'RN':
        break
    if person is 'GV':
        continue
    print(f"Current person: {person}")


# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(i)
# While loops execute a set of statements as long as a condition is true.

count = 0
while(count < 10):
    print(f"Value of count is: {count}")
    count += 1