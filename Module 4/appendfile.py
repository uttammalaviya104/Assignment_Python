# Write a Python program to append text to a file and display the text. 

txt_file = open("textfile.txt","r+")
print(txt_file.read())
txt_file.write("\n ___Written by Uttam Malaviya___ ")
print(txt_file.read())
txt_file.close()
    
