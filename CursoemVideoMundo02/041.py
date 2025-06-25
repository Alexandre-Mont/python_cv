#Classificação de atletas
from datetime import date
atual = date.today() .year
nascimento = int(input("Digite o ano de nascimento: "))
idade = atual - nascimento
if idade <= 9:
    print("Sua idade é {}, você é MIRIM".format(idade))
elif idade <= 14:
    print("Você tem {} e é INFANTIL".format(idade))
elif idade <= 19:
    print("Você tem {} e é JUNIOR".format(idade))
elif idade <= 25:
    print("Você tem {} e é SENHOR".format(idade))
elif idade > 25:
    print("Você tem {} e é MASTER".format(idade))
else:
    print("sua idade não pertime participar")




'''if idade > 7 and idade < 9:
    print("Sua idade é {}, você é MIRIM".format(idade))
elif idade > 9 and idade < 15:
    print("Você tem {} e é INFANTIL".format(idade))
elif idade > 15 and idade <20:
    print("Você tem {} e é JUNIOR".format(idade))
elif idade > 19 and idade < 26:
    print("Você tem {} e é SENHOR".format(idade))
elif idade > 25:
    print("Você tem {} e é MASTER".format(idade))
else:
    print("sua idade não pertime participar")'''