#Desconto 
produto = float(input('Qual o valor do produto'))
desconto = float(input('Digite o desconto'))

valorDesconto = produto * desconto /100
print('Valor de seu desconto {} %'.format(valorDesconto))

print("valor final r$ {}".format(produto-valorDesconto))
