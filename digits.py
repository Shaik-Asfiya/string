...
Write a Python Program to calculate the number of digits and letters in a string.
...
alpha,string=0,"Asfiya"
for i in string:
    if (i.isalpha()):
        alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of Alphabets is", alpha)
