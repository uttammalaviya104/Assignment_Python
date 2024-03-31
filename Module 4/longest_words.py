# Write a python program to find the longest words.

def find_longest_word(text):
    words = text.split()
    print(words)
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word        

text = "Hello My Name is Uttam Malaviya."
longest_word = find_longest_word(text)
print("Longest Word Is: ",longest_word)
print("\n")