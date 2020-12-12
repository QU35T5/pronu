#Skriv ett program med en meny sådan att användaren kan väja att 1)
# skriva ut en fil, 2) lägga till en rad till filen, 3) skriva över filen, och 4) lämna programmet.
def meny():
   print('[1] Skriv ut en fil.')
   print('[2] Lägga till en rad till filen?')
   print('[3] Skriva över filen?')
   print('[4] lämna programmet')

def val_1():
    # öppnar1 filen minfil.txt och skriver ut den
    f = open('minfil.txt','r')
    print('filens innehåll är :')
    
    while True:
        s = f.readline()

        if not s:
            break
        
        print(s,end='\n')
    f.close()

def val_2():
    # öppnar1 filen minfil.txt och skriver ut den
    f = open('minfil.txt','a')
    f.write('\n')   
    while True:
        s = input('Skriv det du vill lägga till ange "enter" för att sluta: ')

        if s == '':
            break
        f.write(s)
    
    f.close()

    f_ut = open('minfil.txt','r')

    print('----Filens nya innehåll är-----: \n')

    for s in f_ut:
        print(s, end = ' \n') 
    f_ut.close()  
    
def val_3():
    f = open('minfil.txt','w')
       
    while True:
        s = input('Skriv det du vill lägga till ange "enter" för att sluta: ')

        if s == '':
            break
        
        f.write(s)
    
    f.close()

    f_ut = open('minfil.txt','r')

    print('----Filens nya innehåll är-----: \n')

    for s in f_ut:
        print(s,end = '\n') 
    f_ut.close()  
        
    
# skriver ut menyn
meny() 
val = int(input('Skriv in ditt val: '))

while val != 4:
    if val == 1:
        val_1()
    elif val ==2:
        val_2()
    elif val == 3:
        val_3()
    else:
        print('okänt val.')
    print()
    meny() 
    val = int(input('Skriv in ditt val: '))

print('Tack och hejdå.')

