""" Write a Python program to find the maximum and minimum numbers 
from the specified decimal numbers."""

def max(list):
    m = list[0]
    for i in range(len(list)):
        if list[i] > m:
            m = list[i] 
    return m        
def min(list):
    m = list[0]
    for i in range(len(list)):
        if list[i] < m:
            m = list[i] 
    return m   
        
my_list = [1,1.1,10,4,2003,1.2,20,21]
maximum_num = max(my_list)
print("Max num: ",maximum_num)
minimum_num = min(my_list)
print("Min num: ",minimum_num)