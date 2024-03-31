# Write a Python program to unzip a list of tuples into individual lists
list_of_tup = [(1,2,3),(4,5,6),(7,8,9)]
individual_list = []    

for x in list_of_tup:
    for i in range(len(x)):
        individual_list.append(x[i])
print(individual_list)    
    