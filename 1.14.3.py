import numpy as np
# Uppgift 1.14.3

# random matrix with size 4 rader 5 kollumner
a = np.random.randint(11,size=(4,5))

print('\n ---Datorn har generat denna matrisen---\n',a,sep='',end ='\n')
# ------------------------------------------------

# adds every row  
print('\n a) ---summan av varje rad är---\n' )
print(np.sum(a,axis=1,keepdims=True),end ='\n')



#--------------------------------------------------
# adds every column
print('\n b) ---summan av varje kollumn är---\n' )

print(np.sum(a,axis=0,keepdims=True))




#--------------------------------------------------
# För specifik kolumn [r,c] 
print('\n c) ---summan av alla jämna kolumner---\n' )

#array av udda rader och jämna kolumner
j = a[:, 1::2]
#print(j)
print('=',np.sum(j,axis=0))# ger summan av alla jämna kollon element() 
# startar från kolumn 0 och går över alla rader och jämna kollumner. 


#--------------------------------------------------

print('\n c) ---Medelvärde för varje kolumn---\n' )
print(np.mean(a,axis = 0)) 

#--------------------------------------------------

print('\n d) ---Medelvärde för alla element i matrisen---\n' )
print(np.mean(a))


#--------------------------------------------------
print('\n e) ---standardavvikelse för alla element i matrisen---\n' )
std = np.std(a)
print(f'= {std:.2f}') 


