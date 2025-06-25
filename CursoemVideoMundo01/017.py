#Catetos e hipotenusa
from math import sqrt,hypot
a = float(input('Compimento do caceto oposto: '))
b = float(input('Comprimento do Cateto adjacente: '))

#h = sqrt(a**2 + b**2) 

hi = hypot(a,b) #BIBLIOTECA MATH COM A FUÇÃO hypot pra

print('A hipotenusa mede {:.2f}'.format(hi))