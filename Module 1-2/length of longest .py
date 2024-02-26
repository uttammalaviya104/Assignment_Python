# Write a Python function that takes a list of words and returns the length of the longest one.
a = input("enter a string:") 
def longest(a):
    max1 = len(a[0])
    temp = a[0]
    for i in a:
        if len(i) > max1:
            max1 = len(i)
            temp = i
    print('longest number is :', temp, 'the length of this word is ', max1)


longest(a)  

