# Kapitel 1: Grundläggande python
# Delkapitel 1.2 arbete med strängar
# Programm som beräknar antal siffror och bokstäver i strängen angiven av användaren

a = input('skriv bokstäver eller hela siffror utan mellanslag: ' ) 
total  = 0 # Startar räkningen med 0 tal
total2 = 0 # Startar räkningen med 0 bokstäver

for i in a:
    if(i.isdigit()): # Boolean, finns hela tal, utför kod nedan.
        total = total + 1 # Loopar igenom alla tal tills det finns inga mer.
    elif len(a): # Retunerar antal bokstäver i a om man skrev bokstäver
        total2 = total2 + 1 # Loopar igenom alla bokstäver tills det inte finns fler
else:
    print('Inte en bokstäver eller tal, skriv heltal.')

print('Du skrev så här många siffor: ', total)
print('Du skrev så här många bokstäver: ', total2)