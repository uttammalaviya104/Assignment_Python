# Write a Python program to check whether a list contains a sub list 
my_list = [10,20,30,[40,50,60]]

for i in my_list:
    print(i) 
    if type(i) == list:
        print("SUB-LIST ARE PRESENT")   
                    