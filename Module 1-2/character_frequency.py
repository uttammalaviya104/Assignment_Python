# Write a prorgram to count the number of character (character frequency) in a string

str = input("Enter a character:")


def function(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)


function(str)
