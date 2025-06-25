#Monta uma lista aleatoria da digitada
import random
print('Quem irá lavar a louça de reunião')
n1 = str(input('Digite o nome do 01 '))
n2 = str(input('Digite o nome do 02 '))
n3 = str(input('Digite o nome do 03 '))
n4 = str(input('Digite o nome do 04 '))

lista = [n1,n2,n3,n4]
soroteio = random.shuffle(lista)

print(lista)
