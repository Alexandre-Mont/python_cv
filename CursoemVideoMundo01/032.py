from datetime import date #biblioteca para ver a data atual
ano = int(input("Que ano você quer análisar?"))
if ano == 0:
    ano = date.today().year #fazendo uma comparação data atual
if ano % 4 == 0 and ano % 100!=0 or ano %400 == 0: #REGRA PARA CÁUCULAR O ANO BISEXTO

    print("O ano {} é BISEXTO" .format(ano))
else:
    print("O ano {} NÃO É BISEXTO".format(ano))

print("fim de execução!")