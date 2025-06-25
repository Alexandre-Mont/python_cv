#reajuste salarial 
salario = float(input("Digite o valor do salário"))
ajuste = float(input("Digite Ajuste"))

valor_ajuste = (salario * ajuste)/100

print("Salário atual {}\n Valor almento {}\n Salário cm ajuste {}".format(salario,valor_ajuste, (salario+valor_ajuste)))


'''
salario = float(input('Digite seu salario: '))
ajuste = float(input('Digite a porcetagem: '))
reajuste = salario * (ajuste / 100)
print(f'O salario atual é R$ {salario:.2f} e com o reajuste será de R$ {reajuste:.2f} e o total ficará em R$ {(salario + reajuste):.2f}')'''