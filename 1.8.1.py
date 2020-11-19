# 
import random

list =[]
for  i in range(0,10):  #range of list is 10
 
    list.append(random.randrange(0,101,2)) #Kollar så det bara är jämna nummer, tal 0 till 100. 
print(list)
    

divisible = [i for i in list if i%7==0 and i%11 ==0 and i%13 == 0 ] # kommer enbart funka för 0.
print(divisible)

