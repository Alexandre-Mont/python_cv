from random import randint #biblioteca para gerar números aéatórios
from time import sleep #biblioteca tempo com o modo esperar 

computador = randint(0,15) #intervamo para os números 
print("<==>" *20)
print("Adivinhe o número que vai aaparecer ")
print("<==>" *20)
jogador = int(input("escola um número de 0 à 15  :"))
print("processando ...")
sleep(3)
if jogador == computador:
    print("Voce acertou {}".format(computador))
else:
    print("Tente novamente {} e você escolheu {}" .format(computador,jogador))