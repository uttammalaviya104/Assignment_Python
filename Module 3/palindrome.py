
#write a python fun to checks whether a passed string is palindrome or not.

def is_palindrome(s):
    if s[0::] == s[::-1]:
        return True
    else:
        return False

ans = is_palindrome('sos')
print(ans)
