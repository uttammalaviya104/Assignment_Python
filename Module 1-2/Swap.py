# Write python program that swap two number with temp variable and without temp variable.

x = int(input("enter the value of x :"))
y = int(input('enter the value of y:'))

temp = x
x = y
y = temp
print('not x value is :', x)
print('not y value is :', y)

