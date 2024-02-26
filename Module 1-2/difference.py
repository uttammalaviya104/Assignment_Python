#Write a Python program that will return true if the two given integer
# values are equal or their sum or difference is 5.

x = int(input("Enter x:"))
y = int(input("Enter y:"))

plus = x + y
dif = x - y


def function(x, y):
    if x == y or plus == 5 or dif == 5:
        print(True)


function(x, y)

