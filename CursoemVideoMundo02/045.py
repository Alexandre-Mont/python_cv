from random import randint #Bibloteca de seleção aleatótia
from time import sleep

Itens = ("Pedra","Papel", "Tesoura")
computador = randint(0,2)
"""print("O computador escolheu {}".format(Itens[computador]))"""
print("""Suas opções:
      [0] Pedra
      [1] Papel
      [2]Tesoura""")
jogador  = int(input("Escolha sua opção: "))
print("JO")
sleep(1)
print(KE)
sleep(1)
print("POO!!!")
print ("-="*11)
print ("O computador escolheu {}".format(Itens[computador]))
print ("Você escolheu {}".format(Itens[jogador]))
print ("-="*11)

if computador == 0:
    if jogador == 0:
        print ("EMPATE")
    elif jogador == 1:
        print ("Voce venceu")
    elif jogador == 2:
        print ("Computador venceu")
    else: 
        print("JOGADA INVALIDA")

elif computador == 1:
    if jogador == 0:
        print("Conputador venceu!")
    elif jogador == 1:
        print ("EMPATE")
    elif jogador == 2:
        print("voCE VENCEU")
    else : print("JOGADA INVALIDA")

elif computador == 2:
    if jogador == 0:
        print("Voce venceu!")
    elif jogador == 1:
        print ("Computador venceu")
    elif jogador == 2:
        print("empate")
    else : print("JOGADA INVALIDA")

    
        
