# Kapitel 1: Grundläggande Python
# Delkapitel 1.4. Rep satser 1
# Uppgift 1.4.3
# Programmet skriver ut multiplikationstabell från 1 till 9 i formen av en
# formaterad tabell.

for i in range(1, 10): # range(start,stop) startar med 1 slutar med 9 och går igenom alla i loopen
    print('\n','Multiplikationstabellen för {} är: '.format(i),'\n') # tar 1 * (1-10) och format(i) är en platshållare som går igenom tal 1-9
    print('-----------------------------------------------------------------------------')

    for m in range(1, 11):                
      print('| ', i * m, end =' \t')   #skriver ut tal 1-9 och 1-10 och multiplicerar med varandra och printar ut hela tabelen, och avslutar varje med ny rad(end =) där \ är tab
    print()

