#analisando o triângulo
r1 = float(input("Digite o valor R1: "))
r2 = float(input("Digite o valor R2: "))
r3 = float(input("Digite o valor R3: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print("Pode formar um triangulo")
else:
    print("não pode formar un triangulo")

'''if r1 == r2 and r3:
    print("é um triangulo")
else:2
    print("não é un triangulo")'''