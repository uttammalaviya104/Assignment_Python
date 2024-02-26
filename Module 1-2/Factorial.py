 #Write a Python program to get the Factorial number of given number.

num = int(input("Enter Number:"))
factorial = 1
if num < 0:
    print("we can't find factorial")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial) 