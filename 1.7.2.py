# Program to multiply two matrices

m = int(input('Hur många rader vill du ha i din första matris?: '))
n = int(input('Hur många kolloner vill du ha i din första matris?: '))

A1=[] #skapar en tom matris

for i in range(0,m): #tar element i
    A1.append([]) # lägger till nya tal i matrisen A1 tills vi når m. 
for i in range(0,m):
    for j in range(0,n):
        A1[i].append([j]) #lägger till nya tal i kollens håll
        A1[i][j] = 0
        print('Skriv in ditt tal i rad', i+1,' kollon: ',j+1)
        A1[i][j]=int(input())
print(A1)

a = int(input('Hur många rader vill du ha i din andra matris?: '))
b = int(input('Hur många kolloner vill du ha i din andra matris?: '))

A2 = [] #skapar en tom matris

for i in range(0,a):
    A2.append([]) # lägger till nya tal i matrislistan i en loop.
for i in range(0,a):
    for j in range(0,b):
        A2[i].append([j]) #lägger till nya tal i kollens håll
        A2[i][j] = 0
        print('Skriv in ditt tal i rad', i+1,' kollon: ',j+1)
        A2[i][j]= int(input())
print(A2) 

if (n==a): #Om antal columner i M1 == antal rader i M2
    C = []
    for i in range(0,m):
        C.append([])
    for i in range(0,m):
        for j in range(0,b):
            C[i].append(j)
            C[i][j]=0

    for a in range(len(A1)):
        for b in range(len(A2[0])):
            for r in range(len(A2)):
                C[a][b] += A1[a][r]*A2[r][b]
    print(C)
else:
    print('Inte möjligt med matrismultiplikation.')

