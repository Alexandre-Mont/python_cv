#SENO, COSENO E TAMGNETE
from math import radians, cos, tan, sin

ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
print('O ângudo de {} tem o  SENO de {:.2f} '.format(ang,seno))
cosseno = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f} '.format(ang,cosseno))
tangente = tan(radians(ang))
print('O ângulo de {} tem a teangente de {:.2f} '.format(ang,tangente))
