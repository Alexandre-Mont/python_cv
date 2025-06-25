#Quebrado o numero
from math import trunc,sqrt
n = float(input('Digite o numero'))
raiz = sqrt(n)

print('Valor de n {} , valor arredondado {}'.format(n, trunc(raiz)))