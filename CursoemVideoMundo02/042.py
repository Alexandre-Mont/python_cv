#Determie qual o tii de triangulo
r1 = float(input("Digite o Primeiro seguimento de reta: "))
r2 = float(input("Digite o Segundo  seguimento de reta: "))
r3 = float(input("Digite o Terceiro seguimento de reta: "))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print("Os seguimento de reta podem formr um triangulo", end=" ") #end serve para unir duas linhas na hora de print
    if r1 == r2 and r2 == r3:
        print(" EQUILATERO")
    if r1 != r2 and r2 != r3 !=r1:
        print("ESCALENO")
    else:
        print("SÔSCELES")
    
else:
    print("As retas não formam um triangulo")