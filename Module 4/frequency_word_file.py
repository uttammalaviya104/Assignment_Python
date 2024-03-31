# Write a Python program to count the frequency of words in a file.
from collections import Counter
def count_freq_words(file):
    with open(file,"r") as filename:
        return Counter(filename.read().split())
    
words_count = count_freq_words("textfile.txt")   
print(words_count)     