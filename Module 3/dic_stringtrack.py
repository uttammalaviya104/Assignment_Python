"""Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1 """

string = 'w3resource'

my_dict = {}
for s in string:
    my_dict[s] = string.count(s)
print(my_dict)
