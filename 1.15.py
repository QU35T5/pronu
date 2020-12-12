#Skapa en 4 x 5 matris med slumpmässiga heltal mellan -10 och 10. Med
#hjälp av logisk indexering, 1) hitta index för element som är större än noll, 2) skriv ut negativa
#heltal, och 3) ersätta negativa heltal med deras absolutbelopp.
import numpy as np
A = np.random.randint(-9,9,(4,5))
print('\n Min matris är:\n',A)
print('värden större än 0 =',A[A>0])
print('deras index är: \n',np.transpose(np.nonzero(A>0)))
print('------------------------------------------------')

print('Negativa heltal =',A[A<0])
print('------------------------------------------------')
print('Replacing\n',np.absolute(A))


