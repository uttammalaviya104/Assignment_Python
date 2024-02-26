# Write a Python program to check if a number is positive, negative or Zero.

a = int(input("Enter a Number:")) 

if a < 0:
    print(a, " : is Negative number")
elif a == 0:
    print(a, " : Zero Number")
else:
    print(a, " is  Positive number")    