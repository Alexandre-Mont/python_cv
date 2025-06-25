#programa para alistamentoano
from datetime import date
atual = date.today().year
nascimento = int(input("Digite o ano de nascimento: "))
idade = atual - nascimento
print("Quem nasceu em {} tem {} anos em {} ".format(nascimento,idade,atual))

if atual == 18:
    print("Você tem de se alistar IMEDIATAMENTE!")
elif atual < 18:
    saldo = idade - 18
    print("Ainda faltam {} paar seu alistamento" .format(saldo))
elif atual > 18:
    saldo = idade - 18
    print("Suda idade é {}, você ja passou {} anos do alistamento" .format(idade,saldo))
