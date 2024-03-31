# Write a Python program to remove an empty tuple(s) from a list of tuples.

my_list = [(1,2,3),(),(4,5,6),(),(7,8,9),(),(10,11,12)] 
bracket_count = my_list.count(())
for i in range(bracket_count):
    my_list.remove(())   
print(my_list)        