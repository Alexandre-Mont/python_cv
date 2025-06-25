#Valida se um número é par ou impar []
numero = int(input("Digite um numero inteiro :"))

resultado = numero % 2 #mostra o resto da divisão 

if resultado == 0:
    print("Esse número {} é PAR!".format(numero))
else:
    print("Esse número {} é IMPAR!".format(numero))
