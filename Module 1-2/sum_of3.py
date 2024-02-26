# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero
x, y, z = int(input("Enter x:")), int(input("Enter y:")), int(input("Enter z:"))

if x == y or y == z or z == x:
    plus = 0
    print(plus)
else:
    plus = x + y + z
    print('sum: ', plus)