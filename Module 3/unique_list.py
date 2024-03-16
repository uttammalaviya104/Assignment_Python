""" Write a Python function that takes a list and returns a new list with unique 
elements of the first list"""

def unique_element(lst):
    x=[]
    for i in lst:
        if i not in x:
            x.append(i)
    return x

print(unique_element([1,2,3,2,2,1,4,3,3,5,6,5,5,3,2,1,7,8,9,0,11,3,4,5,6,7,8,6,7,8,10])) 
print(unique_element([1,True]))
print(unique_element([1,2,3,False,True,0]))