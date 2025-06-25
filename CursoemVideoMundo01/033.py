# Faça um programa que insira 3 números e mostre qual é o maior e o menor

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Verificando o menor valor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

# Verificando o maior valor
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print("Menor valor digitado foi {}".format(menor))
print("Maior valor digitado foi {}".format(maior))
