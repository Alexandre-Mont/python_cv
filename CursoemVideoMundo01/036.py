#Estrutura concicional anunhada
valorimovel = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do sasário :" ))
anosfinanciamento = int(input("Em quantos anos quer pagar a casa?: "))


parcela = valorimovel / (anosfinanciamento *12)

#mesestotal = anosfinanciamento * 12
#250valormensalidade = valorimovel / mesestotal
print("Seu salario é de r${:.2f}, o valor do imóvel é de r$ {:.2f} e a mensalidade é de r${:.2f}".format(salario,valorimovel,parcela))

if parcela >= salario * 30/100:
    print ("não pode fazer ")
else:
    print("Pode fazer ")