""" Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30. """

sqrt=[i**2 for i in range(1,31)]
final_list=sqrt[:5]+sqrt[-5:]

print(final_list)

