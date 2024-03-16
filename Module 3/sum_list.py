#Write a  python function  to get the largest,smallest and sum of all from list.

def large_num(my_list: list):  
    l1 = 0
    l2 = 0
    big = 0
    for i in range(0,len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            l1 = my_list[i]
        else:
            l2 = my_list[i+1]
        if l1>l2:
            if big>l1:
                big = big
            else:
                big = l1    
        else:
            if big>l2:
                big = big
            else:
                big = l2           
    return big           

def big_num(my_list: list): 
    return max(my_list)

def largenum(my_list: list):
    m = my_list[0]
    for x in my_list:
        if x > m:
            m = x
    return m        

def smallnum(my_list: list):
    s = my_list[0]
    for x in my_list:
        if x < s:
            s = x
    return s                

def sum(my_list: list):
    s = 0
    for i in my_list:
        s = s + i
    return s    

my_list = [10,20,30,40,50,60,70,80,90,100]
a = large_num(my_list)
print("largest_num: ",a)
b = big_num(my_list)
print("big_num: ",b)
c = largenum(my_list)
print("largenum: ",c)
d = smallnum(my_list)
print("smallnum: ",d)
e = sum(my_list)
print("sum: ",e)