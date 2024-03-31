# Write a Python program to map two lists into a dictionary 

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [10,20,30,40,50,60,70,80,90,100]
my_dict = {}
x = 0
for i in l1:
    my_dict[i] = l2[x]
    x = x + 1
print(my_dict)   