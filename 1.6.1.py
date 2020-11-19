# Kapitel 1: Grundläggande Python
# Delkapitel 1.6. Tupler och listor
# Uppgift 1.6.3

# Om A = [listan given] representerar 0 postion 1 och 1 postition 2 etc. , 

#a) A[1:3] kommer ge första elementet från det första indexet till det andra. = 4 och 1 , 10 och 3 för tuple. 

# b) A[3:1:-1] start 3 värdet stop 1 men -1 så man får egentligen index 2 inte 1.(end så 2a och vänd stringen. negativ indexering med -1 ger  , samma för tuple for 20 och 3. lägger på en etta om det är reverse på stop.

# c) A[-1::-1] start sista värdet, går igenom hela baklänges. [34,12,10 osv], för tuple, från sista till slutet i reverse. (2,20,3,10,5)
#följande uttryck:

# d) A[len(A):-1:1] tar längden av A vilket är 7 och försöker ta sista värdet -1 men vi kan inte starta från 7 då vårt sista värde är 6. samma här ger tom. väljer ett tomt värde.

# e) dock funkar det här för nu tar den fron 4 till hur än stor listan är istället för att börja på ett värde som inte finns. (10,3,20,2)

# f)  lägger till 10 i slutet av listan funkar ej för tuple den har ej support för det.

# för tuple 

A = (5,10,3,20,2) #[35,12,10,0,1,4,5]
A.append(10)
print(A)
m = int(input('Skriv in antal rader:'))
n = int(input('Skriv in antal kolumner'))
M = []
for 
for i in range(0,m):
    M.append([])
for i in range(0,m):
    for j in range(0,n):
        M[i].append(j)
        M[i][j]= 0
for i in range(0,m):
    for j in range(0,n):
        print('tal i rad:',i+1,'tal i kolumn: ',j+1)
        M[i][j] = int(input())
print(M)