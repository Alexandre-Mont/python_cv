#média do aluno
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print(" Sua média é {:.1f}, você está aprovado".format(media))
elif media >= 5 and media < 7:
    print("Sua nédia é {:.1f}, vovcê está de RECUPERAÇÃO".format(media))

else:
    print("Sua médiai é {:.1f}, você está REPROVADO".format(media))
