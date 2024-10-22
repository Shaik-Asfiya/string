...
 Write a Python Program to form a new string made of the first 2 characters and last 2 characters from a given string.
...
inputString = "Hello world"
 
count = 0
 
# Loop through the string
for i in inputString:
      count = count + 1
newString = inputString[ 0:2 ] + inputString [count - 2: count ] 
 
# Printing the new String
print("Input string = " + inputString)
print("New String = "+ newString)
