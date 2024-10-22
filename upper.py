...
 There are 50 students in the class. The teacher wants to arrange them in the height order. So help the teacher to find the smallest person and tallest to arrange.(count the number of lowercase letters and uppercase letters in a string.)
Problem Description:
The program takes a string and counts the number of lowercase letters and uppercase letters in the string.
...
def Count(str):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
        elif str[i].isdigit():
            number += 1
        else:
            special += 1
    print('Upper case letters:', upper)
    print('Lower case letters:', lower)
    print('Number:', number)
    print('Special characters:', special)
 
# Driver Code
str = "Asfiya"
Count(str)
 
