#write a python fun to check whether a number is perfect or not.

def isperfect_num(num):
    divisable = []
    for i in range(1,int(num/2)+1):
        if num%i == 0:
            divisable.append(i)
    print(divisable)
    if sum(divisable) == num:
        return True
    else:
        return False
        
ans = isperfect_num(6) 
print(ans)            