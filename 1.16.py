# Skapa ett program som ritar de 5 olympiska ringarna.
import numpy as np
import matplotlib.pyplot as plt
# Skapa ett program som ritar en godtycklig kurva. Programmet har en
# meny sådant att användaren kan välja: 1) linjestil, 2) linjefärg, 3) markör, 4) linjetjocklek, 5)
# gränser för x- och y-axel, och 6) figurtitel.
# Plot('x,y,fms,eg1,val1)
def meny():
   print('[1] Linjestil.')
   print('[2] Linjefärg')
   print('[3] Markör')
   print('[4] Linjetjockleck')
   print('[5] Gränser för x-och y-axeln')
   print('[6] Figurtitel')
   print('[7] Lämna programmet.')
   

def val_1():
   anvandare = input("Du kan välja mellan: 'heldragen ','streckad','prickad','streckad-prickad':\n")
   anvandare = anvandare.lower()
   heldragen = 'heldragen'
   streckad = 'streckad'
   prickad = 'prickad' 
   streckad_prickad = 'streckad-prickad'
   if anvandare == heldragen:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price)
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == streckad:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'--')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == prickad:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,':')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()
   elif anvandare == streckad_prickad:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'-.')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()

def val_2():
   anvandare = input("Du kan välja mellan: 'gul ','magenta','cyan','röd','grön','blå','vit','svart':\n")
   anvandare = anvandare.lower()
   gul = 'gul'
   magenta = 'magenta'
   cyan = 'cyan' 
   röd = 'röd'
   grön = 'grön'
   blå = 'blå'
   vit = 'vit' 
   svart = 'svart'
 
   if anvandare == gul:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'y')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == magenta:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'m')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == cyan:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'c')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()
   elif anvandare == röd:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'r')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()

   elif anvandare == grön:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'g')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == blå:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'b')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()
   elif anvandare == vit:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'w')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()
   elif anvandare == svart:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'k')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()

def val_3():
   anvandare = input("Du kan välja mellan: 'cirkel ','plus','Stjärna','punkt','kryss','kvadrat','diamant':\n")
   anvandare = anvandare.lower()
   cirkel = 'cirkel'
   plus = 'plus'
   stjärna = 'stjärna' 
   punkt = 'punkt'
   kryss = 'kryss'
   kvadrat = 'kvadrat'
   diamant = 'diamant' 
   
 
   if anvandare == cirkel:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'o')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == plus:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'+')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == stjärna:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'*')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()
   elif anvandare == punkt:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'.')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()

   elif anvandare == kryss:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'x')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()


   elif anvandare == kvadrat:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'s')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()
   elif anvandare == diamant:
        versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
        year = [2013, 2014, 2015,2016,2017]

        plt.plot(year,versace_price,'d')
        plt.xlabel('Year')
        plt.ylabel('stockprice')
        plt.show()

def val_4():
     anvandare = int(input("Skriv in din linjetjockleck ett heltal:\n"))
     versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
     year = [2013, 2014, 2015,2016,2017]

     plt.plot(year,versace_price,linewidth=anvandare)
     plt.xlabel('Year')
     plt.ylabel('stockprice')
     plt.show()

def val_5():
     xmax = int(input("Vad ska x-axeln ha för gräns? skriv max:\n"))
     xmin = int(input("Vad ska x-axeln ha för gräns? skriv min:\n"))
     ymax = int(input("Vad ska y-axeln ha för gräns? skriv max:\n"))
     ymin = int(input("Vad ska y-axeln ha för gräns? skriv min:\n"))
   
   
     versace_price= [10, 10.95, 55.55, 99.33 , 345.4]
     random_data = [55, 25, 88,105,300]

     plt.plot(random_data,versace_price)
     plt.xlabel('Year')
     plt.ylabel('stockprice')
     plt.xlim([xmin,xmax])
     plt.ylim([ymin,ymax])
     plt.show()
def val_6():
     figur_titel = input('Skriv in din figurtitel:\n')
     versace_price= [10, 100.95, 55.55, 99.33 , 345.4]
     year = [2013, 2014, 2015,2016,2017]

     plt.plot(year,versace_price)
     plt.title(figur_titel)
     plt.xlabel('Year')
     plt.ylabel('stockprice')
     plt.show()

meny() 
val = int(input('Skriv in ditt val: '))

while val != 7:
    if val == 1:
        val_1()
    elif val ==2:
        val_2()
    elif val == 3:
         val_3()
    elif val ==4:
        val_4()
    elif val == 5:
         val_5()
    elif val == 6:
         val_6()
    else:
        print('okänt val.')
    print()    
    meny() 
    val = int(input('Skriv in ditt val: '))
    
    
print('Tack och hejdå.')

