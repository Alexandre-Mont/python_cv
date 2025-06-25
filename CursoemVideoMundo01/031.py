#Custo de viagem
viagem = float(input("Digite a diatância em km: "))

if viagem >= 200:
    preco = viagem * 0.45
else:
    preco = viagem * 0.50

print("Sua distância é de {} e seu valor e R$ {:.2f}".format(viagem,preco))

