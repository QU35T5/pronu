from math import sqrt
# Kapitel 1: Grundläggande Python
# Delkapitel 1.1. Printing
# Uppgift 1.1.1 
# Lös andragradsekvationen ax^2 +bx + c = 0

print('Hej!, nu ska vi lösa en andragradsekvation med a,b och c valt av dig!')

a = float(input('Vilken variabel vill du ha för a? '))
b = float(input('Vilken variabel vill du ha för b? '))
c = float(input('Vilken variabel vill du ha för c? '))

d = (b**2)-(4*a*c) #diskriminanten, rötterna för en andragradare med reela koofecienter är reela
# och distinkta om disktriminanten är positiv, reell med åtminstånde två rötter om den är = 0, och  ger komplexa rötter om den är negativ.


if d < 0: # om diskriminanten är mindre än noll finns inga svar
    print('Tyvärr finns det inga lösningar. Diskriminanten blir mindre än noll, pröva igen.')
    exit() #avbryter scriptet
   
    
elif d == 0: # Om diskriminanten = 0 får man endast en rot
    x = (-b) / 2*a
    print(f'Det finns endast en rot: {x:3}') 

else: # d > 0 två rötter
    x_1 = (-b + sqrt(d)) / (2*a)
    x_2 = (-b - sqrt(d)) / (2*a)
    print (f'Det finns två rötter: {x_1:3} och {x_2:3}') # formaterad sträng, skriver ut tal med 3 tecken
