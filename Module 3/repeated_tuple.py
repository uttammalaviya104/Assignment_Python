#Write a Python program to find the repeated items of a tuple. 

my_tuple = (10,20,20,30,40,30,50,50,100)
unique = []
repeated = []
a = 0
b = 0
for x in my_tuple:
    if x not in unique:
        unique.append(x)
    else:
        repeated.append(x)   
print(unique)         
print("Repeated items: ",repeated)         