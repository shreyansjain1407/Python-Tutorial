# Python has functions for creating, reading, updating, and deleting files.
#Open a file
myFile = open('myFile.txt', 'w') #This will create a file and w stands for wriet

#Get Info about the file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)
# print('Name: ', myFile.name)

#Write to file
myFile.write("Something that's written to the file")
myFile.write("\nSomething else that I wanted to write")
myFile.close()

#Append to file after closed
myFile = open('myFile.txt', 'a') #This will open a file in append mode
myFile.write("\nSomething else that I wanted to write as well")
myFile.close()

#Reading the file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100) #Number of characters
myFile.close()