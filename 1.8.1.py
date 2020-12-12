# Kapitel 1: Grundläggande Python
# Delkapitel 1.8 Comprehension listor
# Uppgift 1.8.1

import random
# Skapar en tom lista 
list =[]
# Skapar en range för i som är max 10.
for  i in range(0,10):  
    # Gör en random range med endast jämna tal från 0 till 100.
    list.append(random.randrange(0,101,2))  
print(list)
    
# kommer enbart funka för 0 om modulo == 0 går det att dela. För vi endast använder jämna tal. 
divisible = [i for i in list if i%7==0 or i%11 ==0 or i%13 == 0 ] 
print('tal som är dividerbara med 7,11 och 13 är',divisible)

