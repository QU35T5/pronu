# Kapitel 1: Grundläggande Python
# Delkapitel 1.9 Funktioner del 1
# Uppgift 1.9.3

def primtal(n):
   # Först kollar vi om värdet av n är mindre än 2, ett primtal är inte 0 och 1.
   if (n<2):
       return False
    # Är talet större än eller = 2 kör loop 
   for i in range(2,n):
       # Om talet ger rest som är == 0, ett tal är ett primtal om det är endast helt  dividerbart med sig självt och 1. 
        if (n%i==0):
            return False
   return True
   
mitttal = int(input('Skriv ett tal: '))
if (primtal(mitttal)):
    print(mitttal,'är ett primtal!')
else: 
        print(mitttal,'är tyvärr inte inte ett primtal.')
print()



