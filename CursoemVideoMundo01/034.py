#aumentos multiplos
salario = float(input("Digite o valor do salário  "))
if salario >= 1200:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)

print("Seu salário ajustado e   {}".format(novo))
