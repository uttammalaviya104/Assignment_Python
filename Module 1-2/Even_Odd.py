# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

x = int(input("Enter Number:"))


def evenodd(x):
    if x % 2 == 0:
        print("your value is even number")
    else:
        if x % 2 != 0:
            print("your value is even")


print(evenodd(x))