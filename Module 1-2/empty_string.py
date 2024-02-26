# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the empty string.
# Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

def string(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]

sample_string_1 = 'w3resource'
result_1 = string(sample_string_1)
print(result_1)

sample_string_2 = 'w3'
result_2 = string(sample_string_2)
print(result_2) 

sample_string_3 = ' w'
result_3 = string(sample_string_3)
print(result_3)
