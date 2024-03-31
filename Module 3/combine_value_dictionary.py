# Write a Python program to combine values in python list of dictionaries

list_of_dictionaries = [{'item':'item1','amount':400},{'item':'item2','amount':690},{'item':'item1','amount':1150}]
l = list_of_dictionaries

Counter = ()
new_dict = {}
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i].get('item') == l[j].get('item'):
            new_dict[l[i].get('item')] = l[i].get('amount') + l[j].get('amount')
        else:
            new_dict[l[i].get('item')] = l[i].get('amount')  
print(new_dict)   
Counter = (new_dict,)
print("Counter",Counter)  