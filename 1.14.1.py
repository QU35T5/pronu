import numpy as np
#Beräkna summan av
#1) alla element med jämna index,

a = np.linspace(12,19,200,dtype=int)
print()
print('Vektorn blir:\n',a.astype(int))


print('\n 1) summan av alla element med udda index är: \n' )
j = a[1::2]
# print('\n dem udda är:\n',j)
print('=',np.sum(j))

print('\n 2) summan av alla element med jämna index är: \n' )
v = a[::2]
#print('\n dem jämna är:\n',v)
print('=',np.sum(v)) 

divisible_by_10 = a[(a%2==0) & (a&5==0)]
print('\n 3) Dessa går att dividera med 10: \n',divisible_by_10)
print('\n Summan av dem =',np.sum(divisible_by_10))

indeces = a[[1,4,18,91]]
print('4) indexens värde är: ')
print('\n',a[1]) #second element
print('\n',a[4]) # 5th element   
print('\n',a[18]) # 19th element
print('\n',a[91])

print('Summan av dessa index är: =\n',np.sum(indeces))