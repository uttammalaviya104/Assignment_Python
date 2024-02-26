# Write a Python program to get the Fibonacci series of given range.

inp = int(input("fibonacci :"))
n1, n2 = 0, 1
count = 0
if inp <= 0:
    print('please enter positive number')
elif inp == 1:
    print(n1)
    print(inp)
else: 
    print("fibonacci")
    while count < inp:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1






