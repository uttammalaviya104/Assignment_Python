#write a python program to write a list to a file.

my_list = ["Uttam",10,2003,4,"Happy",2004]
my_file = open("myfile.txt","w")
my_file.write(str(my_list))
my_file.close()

my_file = open("myfile.txt","r")
print(my_file.read())
my_file.close()