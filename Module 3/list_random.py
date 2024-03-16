# Write a Python program to select an item randomly from a list.
import random
print(random.randint(1, 50))
print(random.choice([1, 3, 1020, 69, True, False, "python", "uttam", 10, 4 ]))
l=[]                           
lucky=[]                        

for i in range(1,101):     
     l.append(i)

for i in range(10):              
     num=random.choice(l)         
     lucky.append(num)           
     l.remove(num)                

print(l)
print(lucky)