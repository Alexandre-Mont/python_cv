#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
#Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
autura = float(input("Digite sua Altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/(autura ** 2)
print("Sua autura é {:.2f}, e seu peso é {:.2f} seu IMC é {:.2f}".format(autura,peso,imc))
print(20*"---")

if imc < 18.5:
    print("MAGREZA")
elif 18.6 <= imc < 24.9:
    print("Normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <=  imc < 39.9:
    print("OBESO")
else:
    print("Vai morrer")