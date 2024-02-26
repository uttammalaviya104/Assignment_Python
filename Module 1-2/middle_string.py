# Write a Python function to insert a string in the middle of a string.

test_str = 'car is for race'

print('the original sring ' + str(test_str))
mid_str = 'good'

temp = test_str.split()
mid_pos = len(temp) // 2

res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]
res = ' '.join(res)
print('formated: ', res)