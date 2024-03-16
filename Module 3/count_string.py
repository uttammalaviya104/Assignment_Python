""" Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings."""

def countstr(lst: list):
    count = 0
    for s in lst:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count         
    
l = ['uttam','dhruv','happy','junagadh']
count = countstr(l)
print(count)  