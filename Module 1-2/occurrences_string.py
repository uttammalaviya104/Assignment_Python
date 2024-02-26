# Write a Python program to count occurrences of a substring in a string.

string = input("Enter a string:")
sub = input("Enter a sub:")
count = 0
for i in range(0, len(string)):
    stat = i
    end = i + len(sub)
    count = count + string.count(sub, stat, end)
print(count)

